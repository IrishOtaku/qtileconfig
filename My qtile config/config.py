# Welcome to my qtile setup








from libqtile import layout, bar, widget
from libqtile.config import Key, Group, Screen, Match
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.widgets import TaskList, ScreenReconfig, SpawnCommand
#from libqtile.layout import Match

mod = "mod4"
terminal = guess_terminal()

# Key bindings
keys = [
    #Key([mod], "h", lazy.layout.left(), desc="Move focus left"),
    #Key([mod], "l", lazy.layout.right(), desc="Move focus right"),
    #Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    #Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "q", lazy.window.kill(), desc="Kill window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating mode for the focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen mode for the focused window"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),




    # Add Applications to to keybinds here
    #Key([mod], "a", lazy.spawn("your_application_command"), desc="Launch Your Application"),

    # Group and Window navigation
    *[Key([mod], str(i), lazy.group[i].toscreen(), desc=f"Switch to group {i}") for i in range(1, 10)],
    *[Key([mod, "shift"], str(i), lazy.window.togroup(i), desc=f"Move window to group {i}") for i in range(1, 10)],  
]

# Workspaces
groups = [Group(str(i)) for i in range(1, 10)]

for i in groups:
    keys.extend(
        [
            # mod1 + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

# Layouts
layouts = [
    layout.MonadTall(
    border_width=1, 
    margin=5),
    border_focus="#0000FF"
    border_normal="#FFFFFF"
    gaps=10, 
    # Layouts to try out
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# Floating layout
floating_layout = Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # Example floating rules
        Match(wm_class="makebranch"),   # Example floating rules
        Match(wm_class="ssh-askpass"),  # Example floating rules
    ],
    border_width=1,
)

# Mouse actions for floating layouts
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True


# For Steam games that want to maximize or a game or application when losing the focus, should we respect this or not of this behaviour it depends so why this is here 

auto_minimize = True 

wl_window_rules = None

wmname = "LG3D"

# Bar setup
widget_defaults = dict(
font="Hack", 
fontsize=12, 
padding=3, 
fontshadow="#000000", 
fontshadowwidth=1, 
foreground="#FFFFFF", 
background="#000080" # Here 2 last digits stands for the opacity of the bar so this means 80 percent
)


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(),
                widget.WindowName(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
                window.Sep(), # Separator for visual distinction
                SpawmCommand(default_spawn="xterm"),  # Change xterm to your desired default application
                widget.Sep(),  # Separator for visual distinction
                widget.Prompt(),  # For running commands
                widget.Spacer(),  # Add space to the bar
                #widget.NetGraph(),  # Network traffic graph
                #widget.Battery(),  # Battery status
                widget.Volume(),  # Volume status
                widget.Sep(),  # Another separator
                widget.CheckUpdates(),  # Check for system updates
                widget.Backlight(),  # Display backlight status
                widget.TextBox("◀▶", fontsize=24),  # Window Focus Indicator
                widget.QuickExit(),
                widget.Systray(),  # System Tray for application icons
                widget.RunScript(default_font="Hack", command="dmenu_run"),  # Launch applications with dmenu
            ],
            24,
        ),
    ),
]


# Monitor is DP-3 for High Refresh rate and low refresh rate monitor is HDMI-A-1

def set_monitor_positions(): 
    subprocess.Popen("xrandr --output HDMI-A-1 --auto --left-of DP-3 --primary", shell=True)
    subprocess.Popen("xrandr --output DP-3 --auto --right-of HDMI-A-1 --primary", shell=True)





def create_screens():
    return [
        Screen(top=create_bar()),  # Bar for the first screen (HDMI)
        Screen(top=create_bar()),  # Bar for the second screen (DP)


    ]


set_monitor_positions()
screens = create_screens()
