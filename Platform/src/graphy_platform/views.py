from django.shortcuts import render, redirect

from .platform import Platform


platform = Platform()


def get_view(request):
    if 'filepath' not in request.GET or 'data_source' not in request.GET or 'visualizer' not in request.GET:
        return redirect('http://127.0.0.1:8000?filepath=&data_source=JSON&visualizer=SIMPLE')

    filepath: str = request.GET.get('filepath', 'aaa.xml')
    data_source = request.GET.get('data_source', 'XML')
    visualizer = request.GET.get('visualizer', 'SIMPLE')
    platform.set_sources(filepath, data_source, visualizer)

    if filepath.strip() != '':
        platform.load_graph()
    response = platform.render_graph(request)
    plugin_content = response.content.decode()

    return render(request, 'platform_home.html', {'plugin_content': plugin_content})
