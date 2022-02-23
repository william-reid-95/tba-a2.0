#colours
from colorama import init
from colorama import Fore, Back, Style

colour_reset = (Style.RESET_ALL) # resest colour

colour_scene_name = (Fore.GREEN + Style.DIM) # text colours for scene variables

colour_scene_temp = (Fore.MAGENTA + Style.DIM)

colour_scene_light_day = (Fore.BLUE + Style.BRIGHT)
colour_scene_light_night = (Fore.BLUE + Style.DIM)

colour_item_name = (Fore.BLACK + Style.BRIGHT) # text colour for all item names

colour_gear_name = (Fore.CYAN + Style.DIM) # text colour for all gear names

colour_spell_name = (Fore.CYAN + Style.NORMAL) # text colour

colour_enemy_name = (Fore.RED + Style.DIM) # text colour

colour_misc_name = (Fore.BLACK + Style.BRIGHT) # misc. text colour

colour_attribute = (Fore.BLACK + Style.BRIGHT) # misc. text colour
