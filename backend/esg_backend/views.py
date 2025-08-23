from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os


def react_app_view(request):
    """
    Serve the React app's index.html for all frontend routes
    """
    try:
        # Path to the React build index.html
        react_build_path = settings.BASE_DIR.parent / 'frontend' / 'build'
        index_path = react_build_path / 'index.html'
        
        if os.path.exists(index_path):
            with open(index_path, 'r', encoding='utf-8') as f:
                return HttpResponse(f.read(), content_type='text/html')
        else:
            return HttpResponse(
                "React build not found. Please run 'npm run build' in the frontend directory.",
                status=404
            )
    except Exception as e:
        return HttpResponse(f"Error serving React app: {str(e)}", status=500)