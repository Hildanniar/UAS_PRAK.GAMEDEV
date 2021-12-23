from setuptools import setup

setup(
    name="HAPPINESS",
    options = {
        'build_apps': {
            'include_patterns': [
                'textures/*.png',
                '**/*.jpg',
                '**/*.egg',
            ],
            'gui_apps': {
                'happiness': 'main.py',
            },
            'log_filename': '$USER_APPDATA/Happiness/output.log',
            'log_append': False,
            'plugins': [
                'pandagl',
                'p3openal_audio',
            ],
        }
    }
)
