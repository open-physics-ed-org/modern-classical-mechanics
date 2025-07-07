import yaml
from jinja2 import Template
import sys
from pathlib import Path

def render_theme(yaml_path, template_path, output_path):
    with open(yaml_path) as f:
        data = yaml.safe_load(f)
    theme_name = data.get('theme', {}).get('name', 'unknown')
    theme_label = data.get('theme', {}).get('label', theme_name)
    theme_desc = data.get('theme', {}).get('description', '')
    colors = data['colors']
    with open(template_path) as f:
        template = Template(f.read())
    css = f"""/*\nTheme: {theme_label} ({theme_name})\nDescription: {theme_desc}\n*/\n""" + template.render(**colors)
    with open(output_path, 'w') as f:
        f.write(css)

def get_theme_names_from_config(config_path):
    with open(config_path) as f:
        config = yaml.safe_load(f)
    theme_cfg = config.get('theme', {})
    light = theme_cfg.get('light', 'light')
    dark = theme_cfg.get('dark', 'dark')
    return {'light': light, 'dark': dark, 'default': theme_cfg.get('default', 'light')}

if __name__ == "__main__":
    import shutil
    # Defaults
    default_config = "_config.yml"
    default_themes_dir = "static/themes"
    default_output_dir = "static/css"
    default_template = "static/templates/main.css.template"
    default_main_css = "static/css/main.css"
    default_bak_css = "static/css/main.css.bak"

    if len(sys.argv) == 1:
        config_path = default_config
        themes_dir = default_themes_dir
        template_path = default_template
        output_dir = default_output_dir
        main_css = default_main_css
        bak_css = default_bak_css
    elif len(sys.argv) == 5:
        config_path, themes_dir, template_path, output_dir = sys.argv[1:5]
        main_css = str(Path(output_dir) / "main.css")
        bak_css = str(Path(output_dir) / "main.css.bak")
    else:
        print("Usage: python theme_to_css.py [<config.yml> <themes_dir> <template.css> <output_dir>]")
        print("If no arguments are given, defaults are used:")
        print(f"  config: {default_config}\n  themes: {default_themes_dir}\n  template: {default_template}\n  output: {default_output_dir}")
        sys.exit(1)

    # Always copy the ground truth backup
    if Path(bak_css).exists():
        shutil.copy2(bak_css, bak_css + ".old")
    if Path(main_css).exists():
        shutil.copy2(main_css, bak_css)

    theme_names = get_theme_names_from_config(config_path)
    # Render light theme as main.css by default
    yaml_path = Path(themes_dir) / f"{theme_names['light']}.yml"
    render_theme(yaml_path, template_path, main_css)
    # Also render dark theme as theme-dark.css
    yaml_path_dark = Path(themes_dir) / f"{theme_names['dark']}.yml"
    render_theme(yaml_path_dark, template_path, str(Path(output_dir) / "theme-dark.css"))
