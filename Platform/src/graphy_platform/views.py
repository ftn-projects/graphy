import json
import traceback

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .workspace import Workspace
from .platform import Platform


platform = Platform()


def get_view(request: WSGIRequest) -> HttpResponse:
    workspace = Workspace()
    platform.add_workspace(workspace)
    return get_workspace_view(request, workspace.id)


def get_workspace_view(
        request: WSGIRequest,
        workspace_id: int,
        plugin_content: HttpResponse | None = None,
        tree_content: HttpResponse | None = None) -> HttpResponse:
    try:
        workspace = platform.get_workspace(workspace_id)
        if workspace is None:
            workspace = Workspace()

        if plugin_content is None:
            plugin_content = workspace.render_graph_view(request)
        if tree_content is None:
            tree_content = workspace.render_tree_view(request)
        bird_content = render(request, 'bird_view.html')

        queries = [c.serialize() for c in workspace.applied_queries]

        return render(request, 'platform_home.html', {
            'plugin_content': plugin_content.content.decode(),
            'tree_content': tree_content.content.decode(),
            'bird_content': bird_content.content.decode(),
            'workspace_id': workspace_id,
            'filepath': workspace.filepath,
            'data_source': workspace.source_plugin.identifier(),
            'visualizer': workspace.visualizer_plugin.identifier(),
            'applied_queries': json.dumps(queries),
            'node_count': workspace.graph_stats['nodes'],
            'edge_count': workspace.graph_stats['edges']
        })
    except BaseException as e:
        return get_with_error(request, workspace_id, e)


def get_search(request: WSGIRequest, workspace_id: int) -> HttpResponse:
    try:
        workspace = platform.get_workspace(workspace_id)

        search = request.GET.get('search', '').lower()
        attribute = request.GET.get('attribute', '').lower()
        operator = request.GET.get('operator', '').lower()
        parameter = request.GET.get('filter', '').lower()

        if search != '':
            workspace.search_graph(search)
        if attribute != '' and operator != '' and parameter != '':
            workspace.filter_graph(attribute, operator, parameter)

        return redirect('http://127.0.0.1:8000/' + str(workspace_id))
    except BaseException as e:
        return get_with_error(request, workspace_id, e)


def get_initial(request, workspace_id: int):
    try:
        workspace = platform.get_workspace(workspace_id)
        workspace.reset_graph()
        return redirect('http://127.0.0.1:8000/' + str(workspace_id))
    except BaseException as e:
        return get_with_error(request, workspace_id, e)


def load(request: WSGIRequest, workspace_id: int) -> HttpResponse:
    try:
        workspace = platform.get_workspace(workspace_id)
        workspace.filepath = request.GET.get('filepath', '')
        workspace.set_source_plugin(request.GET.get('source_type', ''))
        workspace.load_graph()
        return redirect('http://127.0.0.1:8000/' + str(workspace_id))
    except BaseException as e:
        return get_with_error(request, workspace_id, e)


def change_visualizer(request: WSGIRequest, workspace_id: int) -> HttpResponse:
    try:
        workspace = platform.get_workspace(workspace_id)
        workspace.set_visualizer_plugin(request.GET.get('type', ''))
        return redirect('http://127.0.0.1:8000/' + str(workspace_id))
    except BaseException as e:
        return get_with_error(request, workspace_id, e)


def get_with_error(request: WSGIRequest, workspace_id: int, e: BaseException) -> HttpResponse:
    print(traceback.format_exc())
    plugin_content = render(request, 'error_view.html', {'message': str(e)})
    tree_view = render(request, 'tree_view.html')
    return get_workspace_view(request, workspace_id, plugin_content, tree_view)
