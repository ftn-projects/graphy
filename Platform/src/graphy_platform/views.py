import json

from django.shortcuts import render, redirect

from .platform import Platform

platform = Platform()


def get_view(request):
    # if 'filepath' not in request.GET or 'data_source' not in request.GET or 'visualizer' not in request.GET:
    #     return redirect('http://127.0.0.1:8000?filepath=&data_source=JSON&visualizer=SIMPLE')

    filepath: str = request.GET.get('filepath', 'aaa.xml')
    filepath = 'aaa.xml'
    data_source = request.GET.get('data_source', 'XML')
    data_source = 'XML'
    visualizer = request.GET.get('visualizer', 'SIMPLE')
    platform.set_sources(filepath, data_source, visualizer)

    if filepath.strip() != '':
        platform.load_graph()
    response = platform.render_graph(request)
    plugin_content = response.content.decode()

    response_bird = platform.render_bird_view(request)
    plugin_content_bird = response_bird.content.decode()

    response_tree = platform.render_tree_view(request)
    plugin_content_tree = response_tree.content.decode()


    return render(request, 'platform_home.html',
                  {'plugin_content': plugin_content, 'bird_content': plugin_content_bird, 'tree_content':plugin_content_tree})


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

    response_bird = platform.render_bird_view(request)
    plugin_content_bird = response_bird.content.decode()

    response_tree = platform.render_tree_view(request)
    plugin_content_tree = response_tree.content.decode()

    return render(request, 'platform_home.html',
                  {'plugin_content': plugin_content, 'applied_queries': json.dumps(queries),
                   'bird_content': plugin_content_bird, 'tree_content': plugin_content_tree})


def get_initial(request):
    platform.reset_graph()
    return redirect('http://127.0.0.1:8000')
