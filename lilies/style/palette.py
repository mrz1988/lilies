from .colors import Color


aliases = {"cyan": "aqua"}


def get_color(name):
    name = aliases.get(name) or name
    return palette.get(name)


def rgb(r, g, b):
    return Color(rgb=(r, g, b))


def hsl(h, s, l):
    return Color(hsl=(h, s, l))


palette = {
    "black": Color(rgb=(0, 0, 0), hsl=(0, 0, 0)),
    "maroon": Color(rgb=(128, 0, 0), hsl=(0, 100, 25)),
    "green": Color(rgb=(0, 128, 0), hsl=(120, 100, 25)),
    "olive": Color(rgb=(128, 128, 0), hsl=(60, 100, 25)),
    "navy": Color(rgb=(0, 0, 128), hsl=(240, 100, 25)),
    "purple": Color(rgb=(128, 0, 128), hsl=(300, 100, 25)),
    "teal": Color(rgb=(0, 128, 128), hsl=(180, 100, 25)),
    "silver": Color(rgb=(192, 192, 192), hsl=(0, 0, 75)),
    "grey": Color(rgb=(128, 128, 128), hsl=(0, 0, 50)),
    "red": Color(rgb=(255, 0, 0), hsl=(0, 100, 50)),
    "lime": Color(rgb=(0, 255, 0), hsl=(120, 100, 50)),
    "yellow": Color(rgb=(255, 255, 0), hsl=(60, 100, 50)),
    "blue": Color(rgb=(0, 0, 255), hsl=(240, 100, 50)),
    "fuchsia": Color(rgb=(255, 0, 255), hsl=(300, 100, 50)),
    "aqua": Color(rgb=(0, 255, 255), hsl=(180, 100, 50)),
    "white": Color(rgb=(255, 255, 255), hsl=(0, 0, 100)),
    "grey0": Color(rgb=(0, 0, 0), hsl=(0, 0, 0)),
    "navyblue": Color(rgb=(0, 0, 95), hsl=(240, 100, 18)),
    "darkblue": Color(rgb=(0, 0, 135), hsl=(240, 100, 26)),
    "blue3a": Color(rgb=(0, 0, 175), hsl=(240, 100, 34)),
    "blue3b": Color(rgb=(0, 0, 215), hsl=(240, 100, 42)),
    "blue1": Color(rgb=(0, 0, 255), hsl=(240, 100, 50)),
    "darkgreen": Color(rgb=(0, 95, 0), hsl=(120, 100, 18)),
    "deepskyblue4a": Color(rgb=(0, 95, 95), hsl=(180, 100, 18)),
    "deepskyblue4b": Color(rgb=(0, 95, 135), hsl=(197.777777777778, 100, 26)),
    "deepskyblue4c": Color(rgb=(0, 95, 175), hsl=(207.428571428571, 100, 34)),
    "dodgerblue3": Color(rgb=(0, 95, 215), hsl=(213.488372093023, 100, 42)),
    "dodgerblue2": Color(rgb=(0, 95, 255), hsl=(217.647058823529, 100, 50)),
    "green4": Color(rgb=(0, 135, 0), hsl=(120, 100, 26)),
    "springgreen4": Color(rgb=(0, 135, 95), hsl=(162.222222222222, 100, 26)),
    "turquoise4": Color(rgb=(0, 135, 135), hsl=(180, 100, 26)),
    "deepskyblue3a": Color(rgb=(0, 135, 175), hsl=(193.714285714286, 100, 34)),
    "deepskyblue3b": Color(rgb=(0, 135, 215), hsl=(202.325581395349, 100, 42)),
    "dodgerblue1": Color(rgb=(0, 135, 255), hsl=(208.235294117647, 100, 50)),
    "darkcyan": Color(rgb=(0, 175, 135), hsl=(166.285714285714, 100, 34)),
    "lightseagreen": Color(rgb=(0, 175, 175), hsl=(180, 100, 34)),
    "deepskyblue2": Color(rgb=(0, 175, 215), hsl=(191.162790697674, 100, 42)),
    "deepskyblue1": Color(rgb=(0, 175, 255), hsl=(198.823529411765, 100, 50)),
    "green3a": Color(rgb=(0, 175, 0), hsl=(120, 100, 34)),
    "green3b": Color(rgb=(0, 215, 0), hsl=(120, 100, 42)),
    "springgreen3a": Color(rgb=(0, 175, 95), hsl=(152.571428571429, 100, 34)),
    "springgreen3b": Color(rgb=(0, 215, 95), hsl=(146.511627906977, 100, 42)),
    "cyan3": Color(rgb=(0, 215, 175), hsl=(168.837209302326, 100, 42)),
    "darkturquoise": Color(rgb=(0, 215, 215), hsl=(180, 100, 42)),
    "turquoise2": Color(rgb=(0, 215, 255), hsl=(189.411764705882, 100, 50)),
    "green1": Color(rgb=(0, 255, 0), hsl=(120, 100, 50)),
    "springgreen2a": Color(rgb=(0, 215, 135), hsl=(157.674418604651, 100, 42)),
    "springgreen2b": Color(rgb=(0, 255, 95), hsl=(142.352941176471, 100, 50)),
    "springgreen1": Color(rgb=(0, 255, 135), hsl=(151.764705882353, 100, 50)),
    "mediumspringgreen": Color(
        rgb=(0, 255, 175), hsl=(161.176470588235, 100, 50)
    ),
    "cyan2": Color(rgb=(0, 255, 215), hsl=(170.588235294118, 100, 50)),
    "cyan1": Color(rgb=(0, 255, 255), hsl=(180, 100, 50)),
    "purple4a": Color(rgb=(95, 0, 135), hsl=(282.222222222222, 100, 26)),
    "purple4b": Color(rgb=(95, 0, 175), hsl=(272.571428571429, 100, 34)),
    "purple3": Color(rgb=(95, 0, 215), hsl=(266.511627906977, 100, 42)),
    "blueviolet": Color(rgb=(95, 0, 255), hsl=(262.352941176471, 100, 50)),
    "grey37": Color(rgb=(95, 95, 95), hsl=(0, 0, 37)),
    "mediumpurple4": Color(rgb=(95, 95, 135), hsl=(240, 17, 45)),
    "slateblue3a": Color(rgb=(95, 95, 175), hsl=(240, 33, 52)),
    "slateblue3b": Color(rgb=(95, 95, 215), hsl=(240, 60, 60)),
    "royalblue1": Color(rgb=(95, 95, 255), hsl=(240, 100, 68)),
    "chartreuse4": Color(rgb=(95, 135, 0), hsl=(77.7777777777778, 100, 26)),
    "paleturquoise4": Color(rgb=(95, 135, 135), hsl=(180, 17, 45)),
    "steelblue": Color(rgb=(95, 135, 175), hsl=(210, 33, 52)),
    "steelblue3": Color(rgb=(95, 135, 215), hsl=(220, 60, 60)),
    "cornflowerblue": Color(rgb=(95, 135, 255), hsl=(225, 100, 68)),
    "darkseagreen4a": Color(rgb=(95, 135, 95), hsl=(120, 17, 45)),
    "darkseagreen4b": Color(rgb=(95, 175, 95), hsl=(120, 33, 52)),
    "cadetbluea": Color(rgb=(95, 175, 135), hsl=(150, 33, 52)),
    "cadetblueb": Color(rgb=(95, 175, 175), hsl=(180, 33, 52)),
    "skyblue3": Color(rgb=(95, 175, 215), hsl=(200, 60, 60)),
    "chartreuse3a": Color(rgb=(95, 175, 0), hsl=(87.4285714285714, 100, 34)),
    "chartreuse3b": Color(rgb=(95, 215, 0), hsl=(93.4883720930233, 100, 42)),
    "seagreen3": Color(rgb=(95, 215, 135), hsl=(140, 60, 60)),
    "aquamarine3": Color(rgb=(95, 215, 175), hsl=(160, 60, 60)),
    "mediumturquoise": Color(rgb=(95, 215, 215), hsl=(180, 60, 60)),
    "steelblue1a": Color(rgb=(95, 175, 255), hsl=(210, 100, 68)),
    "steelblue1b": Color(rgb=(95, 215, 255), hsl=(195, 100, 68)),
    "seagreen2": Color(rgb=(95, 255, 95), hsl=(120, 100, 68)),
    "seagreen1a": Color(rgb=(95, 255, 135), hsl=(135, 100, 68)),
    "seagreen1b": Color(rgb=(95, 255, 175), hsl=(150, 100, 68)),
    "darkslategray2": Color(rgb=(95, 255, 255), hsl=(180, 100, 68)),
    "darkreda": Color(rgb=(95, 0, 0), hsl=(0, 100, 18)),
    "darkredb": Color(rgb=(135, 0, 0), hsl=(0, 100, 26)),
    "deeppink4a": Color(rgb=(95, 0, 95), hsl=(300, 100, 18)),
    "deeppink4b": Color(rgb=(135, 0, 95), hsl=(317.777777777778, 100, 26)),
    "darkmagentaa": Color(rgb=(135, 0, 135), hsl=(300, 100, 26)),
    "darkmagentab": Color(rgb=(135, 0, 175), hsl=(286.285714285714, 100, 34)),
    "purplea": Color(rgb=(128, 0, 128), hsl=(300, 100, 25)),
    "purpleb": Color(rgb=(135, 0, 255), hsl=(271.764705882353, 100, 50)),
    "orange4a": Color(rgb=(95, 95, 0), hsl=(60, 100, 18)),
    "orange4b": Color(rgb=(135, 95, 0), hsl=(42.2222222222222, 100, 26)),
    "lightpink4": Color(rgb=(135, 95, 95), hsl=(0, 17, 45)),
    "plum4": Color(rgb=(135, 95, 135), hsl=(300, 17, 45)),
    "mediumpurple3a": Color(rgb=(135, 95, 175), hsl=(270, 33, 52)),
    "mediumpurple3b": Color(rgb=(135, 95, 215), hsl=(260, 60, 60)),
    "slateblue1": Color(rgb=(135, 95, 255), hsl=(255, 100, 68)),
    "wheat4": Color(rgb=(135, 135, 95), hsl=(60, 17, 45)),
    "grey53": Color(rgb=(135, 135, 135), hsl=(0, 0, 52)),
    "lightslategrey": Color(rgb=(135, 135, 175), hsl=(240, 20, 60)),
    "mediumpurple": Color(rgb=(135, 135, 215), hsl=(240, 50, 68)),
    "lightslateblue": Color(rgb=(135, 135, 255), hsl=(240, 100, 76)),
    "yellow4a": Color(rgb=(135, 135, 0), hsl=(60, 100, 26)),
    "yellow4b": Color(rgb=(135, 175, 0), hsl=(73.7142857142857, 100, 34)),
    "darkseagreen": Color(rgb=(135, 175, 135), hsl=(120, 20, 60)),
    "lightskyblue3a": Color(rgb=(135, 175, 175), hsl=(180, 20, 60)),
    "lightskyblue3b": Color(rgb=(135, 175, 215), hsl=(210, 50, 68)),
    "skyblue2": Color(rgb=(135, 175, 255), hsl=(220, 100, 76)),
    "chartreuse2a": Color(rgb=(95, 255, 0), hsl=(97.6470588235294, 100, 50)),
    "chartreuse2b": Color(rgb=(135, 215, 0), hsl=(82.3255813953488, 100, 42)),
    "darkolivegreen3a": Color(rgb=(135, 175, 95), hsl=(90, 33, 52)),
    "darkolivegreen3b": Color(rgb=(135, 215, 95), hsl=(100, 60, 60)),
    "palegreen3a": Color(rgb=(95, 215, 95), hsl=(120, 60, 60)),
    "palegreen3b": Color(rgb=(135, 215, 135), hsl=(120, 50, 68)),
    "darkslategray3": Color(rgb=(135, 215, 215), hsl=(180, 50, 68)),
    "skyblue1": Color(rgb=(135, 215, 255), hsl=(200, 100, 76)),
    "chartreuse1": Color(rgb=(135, 255, 0), hsl=(88.2352941176471, 100, 50)),
    "lightgreena": Color(rgb=(135, 255, 95), hsl=(105, 100, 68)),
    "lightgreenb": Color(rgb=(135, 255, 135), hsl=(120, 100, 76)),
    "aquamarine1a": Color(rgb=(95, 255, 215), hsl=(165, 100, 68)),
    "aquamarine1b": Color(rgb=(135, 255, 215), hsl=(160, 100, 76)),
    "darkslategray1": Color(rgb=(135, 255, 255), hsl=(180, 100, 76)),
    "deeppink4c": Color(rgb=(175, 0, 95), hsl=(327.428571428571, 100, 34)),
    "mediumvioletred": Color(
        rgb=(175, 0, 135), hsl=(313.714285714286, 100, 34)
    ),
    "darkvioleta": Color(rgb=(135, 0, 215), hsl=(277.674418604651, 100, 42)),
    "darkvioletb": Color(rgb=(175, 0, 215), hsl=(288.837209302326, 100, 42)),
    "purplec": Color(rgb=(175, 0, 255), hsl=(281.176470588235, 100, 50)),
    "mediumorchid3": Color(rgb=(175, 95, 175), hsl=(300, 33, 52)),
    "mediumorchid": Color(rgb=(175, 95, 215), hsl=(280, 60, 60)),
    "darkgoldenrod": Color(rgb=(175, 135, 0), hsl=(46.2857142857143, 100, 34)),
    "rosybrown": Color(rgb=(175, 135, 135), hsl=(0, 20, 60)),
    "grey63": Color(rgb=(175, 135, 175), hsl=(300, 20, 60)),
    "mediumpurple2a": Color(rgb=(175, 95, 255), hsl=(270, 100, 68)),
    "mediumpurple2b": Color(rgb=(175, 135, 215), hsl=(270, 50, 68)),
    "mediumpurple1": Color(rgb=(175, 135, 255), hsl=(260, 100, 76)),
    "darkkhaki": Color(rgb=(175, 175, 95), hsl=(60, 33, 52)),
    "navajowhite3": Color(rgb=(175, 175, 135), hsl=(60, 20, 60)),
    "grey69": Color(rgb=(175, 175, 175), hsl=(0, 0, 68)),
    "lightsteelblue3": Color(rgb=(175, 175, 215), hsl=(240, 33, 76)),
    "lightsteelblue": Color(rgb=(175, 175, 255), hsl=(240, 100, 84)),
    "darkolivegreen3c": Color(rgb=(175, 215, 95), hsl=(80, 60, 60)),
    "darkseagreen3a": Color(rgb=(135, 215, 175), hsl=(150, 50, 68)),
    "darkseagreen3b": Color(rgb=(175, 215, 135), hsl=(90, 50, 68)),
    "lightcyan3": Color(rgb=(175, 215, 215), hsl=(180, 33, 76)),
    "lightskyblue1": Color(rgb=(175, 215, 255), hsl=(210, 100, 84)),
    "greenyellow": Color(rgb=(175, 255, 0), hsl=(78.8235294117647, 100, 50)),
    "darkolivegreen2": Color(rgb=(175, 255, 95), hsl=(90, 100, 68)),
    "palegreen1a": Color(rgb=(135, 255, 175), hsl=(140, 100, 76)),
    "palegreen1b": Color(rgb=(175, 255, 135), hsl=(100, 100, 76)),
    "darkseagreen2a": Color(rgb=(175, 215, 175), hsl=(120, 33, 76)),
    "darkseagreen2b": Color(rgb=(175, 255, 175), hsl=(120, 100, 84)),
    "paleturquoise1": Color(rgb=(175, 255, 255), hsl=(180, 100, 84)),
    "red3a": Color(rgb=(175, 0, 0), hsl=(0, 100, 34)),
    "red3b": Color(rgb=(215, 0, 0), hsl=(0, 100, 42)),
    "deeppink3a": Color(rgb=(215, 0, 95), hsl=(333.488372093023, 100, 42)),
    "deeppink3b": Color(rgb=(215, 0, 135), hsl=(322.325581395349, 100, 42)),
    "magenta3a": Color(rgb=(175, 0, 175), hsl=(300, 100, 34)),
    "magenta3b": Color(rgb=(215, 0, 175), hsl=(311.162790697674, 100, 42)),
    "magenta3c": Color(rgb=(215, 0, 215), hsl=(300, 100, 42)),
    "darkorange3a": Color(rgb=(175, 95, 0), hsl=(32.5714285714286, 100, 34)),
    "darkorange3b": Color(rgb=(215, 95, 0), hsl=(26.5116279069767, 100, 42)),
    "indianreda": Color(rgb=(175, 95, 95), hsl=(0, 33, 52)),
    "indianredb": Color(rgb=(215, 95, 95), hsl=(0, 60, 60)),
    "hotpink3a": Color(rgb=(175, 95, 135), hsl=(330, 33, 52)),
    "hotpink3b": Color(rgb=(215, 95, 135), hsl=(340, 60, 60)),
    "hotpink2": Color(rgb=(215, 95, 175), hsl=(320, 60, 60)),
    "orchid": Color(rgb=(215, 95, 215), hsl=(300, 60, 60)),
    "orange3": Color(rgb=(215, 135, 0), hsl=(37.6744186046512, 100, 42)),
    "lightsalmon3a": Color(rgb=(175, 135, 95), hsl=(30, 33, 52)),
    "lightsalmon3b": Color(rgb=(215, 135, 95), hsl=(20, 60, 60)),
    "lightpink3": Color(rgb=(215, 135, 135), hsl=(0, 50, 68)),
    "pink3": Color(rgb=(215, 135, 175), hsl=(330, 50, 68)),
    "plum3": Color(rgb=(215, 135, 215), hsl=(300, 50, 68)),
    "violet": Color(rgb=(215, 135, 255), hsl=(280, 100, 76)),
    "gold3a": Color(rgb=(175, 175, 0), hsl=(60, 100, 34)),
    "gold3b": Color(rgb=(215, 175, 0), hsl=(48.8372093023256, 100, 42)),
    "lightgoldenrod3": Color(rgb=(215, 175, 95), hsl=(40, 60, 60)),
    "tan": Color(rgb=(215, 175, 135), hsl=(30, 50, 68)),
    "mistyrose3": Color(rgb=(215, 175, 175), hsl=(0, 33, 76)),
    "thistle3": Color(rgb=(215, 175, 215), hsl=(300, 33, 76)),
    "plum2": Color(rgb=(215, 175, 255), hsl=(270, 100, 84)),
    "yellow3a": Color(rgb=(175, 215, 0), hsl=(71.1627906976744, 100, 42)),
    "yellow3b": Color(rgb=(215, 215, 0), hsl=(60, 100, 42)),
    "khaki3": Color(rgb=(215, 215, 95), hsl=(60, 60, 60)),
    "lightyellow3": Color(rgb=(215, 215, 175), hsl=(60, 33, 76)),
    "grey84": Color(rgb=(215, 215, 215), hsl=(0, 0, 84)),
    "lightsteelblue1": Color(rgb=(215, 215, 255), hsl=(240, 100, 92)),
    "yellow2": Color(rgb=(215, 255, 0), hsl=(69.4117647058823, 100, 50)),
    "darkolivegreen1a": Color(rgb=(215, 255, 95), hsl=(75, 100, 68)),
    "darkolivegreen1b": Color(rgb=(215, 255, 135), hsl=(80, 100, 76)),
    "darkseagreen1a": Color(rgb=(175, 255, 215), hsl=(150, 100, 84)),
    "darkseagreen1b": Color(rgb=(215, 255, 175), hsl=(90, 100, 84)),
    "honeydew2": Color(rgb=(215, 255, 215), hsl=(120, 100, 92)),
    "lightcyan1": Color(rgb=(215, 255, 255), hsl=(180, 100, 92)),
    "red1": Color(rgb=(255, 0, 0), hsl=(0, 100, 50)),
    "deeppink2": Color(rgb=(255, 0, 95), hsl=(337.647058823529, 100, 50)),
    "deeppink1a": Color(rgb=(255, 0, 135), hsl=(328.235294117647, 100, 50)),
    "deeppink1b": Color(rgb=(255, 0, 175), hsl=(318.823529411765, 100, 50)),
    "magenta2a": Color(rgb=(215, 0, 255), hsl=(290.588235294118, 100, 50)),
    "magenta2b": Color(rgb=(255, 0, 215), hsl=(309.411764705882, 100, 50)),
    "magenta1": Color(rgb=(255, 0, 255), hsl=(300, 100, 50)),
    "orangered1": Color(rgb=(255, 95, 0), hsl=(22.3529411764706, 100, 50)),
    "indianred1a": Color(rgb=(255, 95, 95), hsl=(0, 100, 68)),
    "indianred1b": Color(rgb=(255, 95, 135), hsl=(345, 100, 68)),
    "hotpinka": Color(rgb=(255, 95, 175), hsl=(330, 100, 68)),
    "hotpinkb": Color(rgb=(255, 95, 215), hsl=(315, 100, 68)),
    "mediumorchid1a": Color(rgb=(215, 95, 255), hsl=(285, 100, 68)),
    "mediumorchid1b": Color(rgb=(255, 95, 255), hsl=(300, 100, 68)),
    "darkorange": Color(rgb=(255, 135, 0), hsl=(31.7647058823529, 100, 50)),
    "salmon1": Color(rgb=(255, 135, 95), hsl=(15, 100, 68)),
    "lightcoral": Color(rgb=(255, 135, 135), hsl=(0, 100, 76)),
    "palevioletred1": Color(rgb=(255, 135, 175), hsl=(340, 100, 76)),
    "orchid2": Color(rgb=(255, 135, 215), hsl=(320, 100, 76)),
    "orchid1": Color(rgb=(255, 135, 255), hsl=(300, 100, 76)),
    "orange1": Color(rgb=(255, 175, 0), hsl=(41.1764705882353, 100, 50)),
    "sandybrown": Color(rgb=(255, 175, 95), hsl=(30, 100, 68)),
    "lightsalmon1": Color(rgb=(255, 175, 135), hsl=(20, 100, 76)),
    "lightpink1": Color(rgb=(255, 175, 175), hsl=(0, 100, 84)),
    "pink1": Color(rgb=(255, 175, 215), hsl=(330, 100, 84)),
    "plum1": Color(rgb=(255, 175, 255), hsl=(300, 100, 84)),
    "gold1": Color(rgb=(255, 215, 0), hsl=(50.5882352941176, 100, 50)),
    "lightgoldenrod2a": Color(rgb=(215, 215, 135), hsl=(60, 50, 68)),
    "lightgoldenrod2b": Color(rgb=(255, 215, 95), hsl=(45, 100, 68)),
    "lightgoldenrod2c": Color(rgb=(255, 215, 135), hsl=(40, 100, 76)),
    "navajowhite1": Color(rgb=(255, 215, 175), hsl=(30, 100, 84)),
    "mistyrose1": Color(rgb=(255, 215, 215), hsl=(0, 100, 92)),
    "thistle1": Color(rgb=(255, 215, 255), hsl=(300, 100, 92)),
    "yellow1": Color(rgb=(255, 255, 0), hsl=(60, 100, 50)),
    "lightgoldenrod1": Color(rgb=(255, 255, 95), hsl=(60, 100, 68)),
    "khaki1": Color(rgb=(255, 255, 135), hsl=(60, 100, 76)),
    "wheat1": Color(rgb=(255, 255, 175), hsl=(60, 100, 84)),
    "cornsilk1": Color(rgb=(255, 255, 215), hsl=(60, 100, 92)),
    "grey100": Color(rgb=(255, 255, 255), hsl=(0, 0, 100)),
    "grey3": Color(rgb=(8, 8, 8), hsl=(0, 0, 3)),
    "grey7": Color(rgb=(18, 18, 18), hsl=(0, 0, 7)),
    "grey11": Color(rgb=(28, 28, 28), hsl=(0, 0, 10)),
    "grey15": Color(rgb=(38, 38, 38), hsl=(0, 0, 14)),
    "grey19": Color(rgb=(48, 48, 48), hsl=(0, 0, 18)),
    "grey23": Color(rgb=(58, 58, 58), hsl=(0, 0, 22)),
    "grey27": Color(rgb=(68, 68, 68), hsl=(0, 0, 26)),
    "grey30": Color(rgb=(78, 78, 78), hsl=(0, 0, 30)),
    "grey35": Color(rgb=(88, 88, 88), hsl=(0, 0, 34)),
    "grey39": Color(rgb=(98, 98, 98), hsl=(0, 0, 37)),
    "grey42": Color(rgb=(108, 108, 108), hsl=(0, 0, 40)),
    "grey46": Color(rgb=(118, 118, 118), hsl=(0, 0, 46)),
    "grey50": Color(rgb=(128, 128, 128), hsl=(0, 0, 50)),
    "grey54": Color(rgb=(138, 138, 138), hsl=(0, 0, 54)),
    "grey58": Color(rgb=(148, 148, 148), hsl=(0, 0, 58)),
    "grey62": Color(rgb=(158, 158, 158), hsl=(0, 0, 61)),
    "grey66": Color(rgb=(168, 168, 168), hsl=(0, 0, 65)),
    "grey70": Color(rgb=(178, 178, 178), hsl=(0, 0, 69)),
    "grey74": Color(rgb=(188, 188, 188), hsl=(0, 0, 73)),
    "grey78": Color(rgb=(198, 198, 198), hsl=(0, 0, 77)),
    "grey82": Color(rgb=(208, 208, 208), hsl=(0, 0, 81)),
    "grey85": Color(rgb=(218, 218, 218), hsl=(0, 0, 85)),
    "grey89": Color(rgb=(228, 228, 228), hsl=(0, 0, 89)),
    "grey93": Color(rgb=(238, 238, 238), hsl=(0, 0, 93)),
}


ORDERED_ANSI_16_COLOR_PALETTE = [
    palette["black"],
    palette["maroon"],
    palette["green"],
    palette["olive"],
    palette["navy"],
    palette["purple"],
    palette["teal"],
    palette["silver"],
    palette["grey"],
    palette["red"],
    palette["lime"],
    palette["yellow"],
    palette["blue"],
    palette["fuchsia"],
    palette["aqua"],
    palette["white"],
]


ANSI_16_COLOR_PALETTE = set(ORDERED_ANSI_16_COLOR_PALETTE)
