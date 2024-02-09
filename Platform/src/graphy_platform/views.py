import json

from django.shortcuts import render, redirect

from .workspace import Workspace
from .platform import Platform

platform = Platform()

# def get_view(request):
#     if filepath.strip() != '':
#         platform.load_graph()
#     response = platform.render_graph(request)
#     plugin_content = response.content.decode()

def get_view(request):
    workspace = Workspace()
    platform.addWorkspace(workspace)

    return get_workspace_view(request, workspace.id)

def get_workspace_view(request, id: int):
    workspace = platform.getWorkspace(id)
    queries = [c.serialize() for c in workspace.applied_queries]

    return render(request, 'platform_home.html', {
        'plugin_content': workspace.render_graph(request),
        'workspace_id' : id,
        'filepath' : workspace.filepath,
        'data_source' : workspace.source_plugin.identifier(),
        'visualizer' : workspace.visualizer_plugin.identifier(),
        'applied_queries': json.dumps(queries)
        })


def get_query(request):
    search = request.GET.get('search', '').lower()
    attribute = request.GET.get('attribute', '').lower()
    operator = request.GET.get('operator', '').lower()
    parameter = request.GET.get('filter', '').lower()

    if search != '':
        platform.search_graph(search)
    if attribute != '' and operator != '' and parameter != '':
        platform.filter_graph(attribute, operator, parameter)

    response = platform.render_graph(request)
    plugin_content = response.content.decode()

    queries = [c.serialize() for c in platform.applied_queries]

    return render(request, 'platform_home.html',
                  {'plugin_content': plugin_content, 'applied_queries': json.dumps(queries)})


def get_initial(request):
    platform.reset_graph()
    return redirect('http://127.0.0.1:8000')

