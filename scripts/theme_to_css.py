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
    # Add dark_mode flag for template logic
    css = f"""/*\nTheme: {theme_label} ({theme_name})\nDescription: {theme_desc}\n*/\n""" + template.render(**colors, dark_mode=('dark' in output_path))
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
    # Defaults (use .autogen/_config.yml as canonical config)
    default_config = ".autogen/_config.yml"
    default_themes_dir = "static/themes"
    default_output_dir = "static/css"
    default_template = "static/templates/main.css.template"
    default_light_css = "static/css/theme-light.css"
    default_dark_css = "static/css/theme-dark.css"
    default_bak_css = "static/css/main.css.bak"

    if len(sys.argv) == 1:
        config_path = default_config
        themes_dir = default_themes_dir
        template_path = default_template
        output_dir = default_output_dir
        light_css = default_light_css
        dark_css = default_dark_css
        bak_css = default_bak_css
    elif len(sys.argv) == 5:
        config_path, themes_dir, template_path, output_dir = sys.argv[1:5]
        light_css = str(Path(output_dir) / "theme-light.css")
        dark_css = str(Path(output_dir) / "theme-dark.css")
        bak_css = str(Path(output_dir) / "main.css.bak")
    else:
        print("Usage: python theme_to_css.py [<config.yml> <themes_dir> <template.css> <output_dir>]")
        print("If no arguments are given, defaults are used:")
        print(f"  config: {default_config}\n  themes: {default_themes_dir}\n  template: {default_template}\n  output: {default_output_dir}")
        sys.exit(1)

    # Always copy the ground truth backup for main.css if it exists
    main_css = str(Path(output_dir) / "main.css")
    if Path(bak_css).exists():
        shutil.copy2(bak_css, bak_css + ".old")
    if Path(main_css).exists():
        shutil.copy2(main_css, bak_css)

    theme_names = get_theme_names_from_config(config_path)
    # Debug info
    print(f"[DEBUG] Using config: {config_path}")
    print(f"[DEBUG] Themes dir: {themes_dir}")
    print(f"[DEBUG] Template: {template_path}")
    print(f"[DEBUG] Output dir: {output_dir}")
    # Render light theme as theme-light.css
    yaml_path = Path(themes_dir) / f"{theme_names['light']}.yml"
    if not yaml_path.exists():
        print(f"[ERROR] Light theme YAML not found: {yaml_path}", file=sys.stderr)
        sys.exit(2)
    render_theme(yaml_path, template_path, light_css)
    print(f"[INFO] Rendered light theme: {yaml_path} -> {light_css}")
    # Render dark theme as theme-dark.css
    yaml_path_dark = Path(themes_dir) / f"{theme_names['dark']}.yml"
    if not yaml_path_dark.exists():
        print(f"[ERROR] Dark theme YAML not found: {yaml_path_dark}", file=sys.stderr)
        sys.exit(2)
    render_theme(yaml_path_dark, template_path, dark_css)
    print(f"[INFO] Rendered dark theme: {yaml_path_dark} -> {dark_css}")
