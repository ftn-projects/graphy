from django.shortcuts import render

from .platform import Platform


platform = Platform()


def get_view(request):
    filepath = 'aaa.xml'  # request.GET['filepath']
    data_source = 'XML'  # request.GET['data_source']
    visualizer = 'BLOCK'  # request.GET['visualizer']
    platform.set_sources(filepath, data_source, visualizer)

    platform.load_graph()
    response = platform.render_graph(request)
    plugin_content = response.content.decode()

    return render(request, 'platform_home.html', {'plugin_content': plugin_content})
