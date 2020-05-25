from os import scandir
from odf.opendocument import load


for png in scandir("./input"):
    print(f"Process: {png.name}")
    odt_name = png.name.split('.')[0] + '.odt'
    print(f"    Output name: {odt_name}")

    template = load("template.odt")
    textdoc = template

    del textdoc.Pictures['Pictures/10000000000008BC00000D4A2248334464A78D9E.png']
    png_name = textdoc.addPictureFromFile('./input/' + png.name)

    print(f"    Internal image name: {png_name}")

    for kid in textdoc.styles.childNodes:
        if kid.tagName == 'draw:fill-image':
            print(f"        HREF Old: {kid.attributes[('http://www.w3.org/1999/xlink', 'href')]}")
            kid.attributes[('http://www.w3.org/1999/xlink', 'href')] = png_name
            print(f"        HREF New: {kid.attributes[('http://www.w3.org/1999/xlink', 'href')]}")

    for kid in textdoc.automaticstyles.childNodes:
        if kid.tagName == 'style:page-layout':
            for child in kid.childNodes:
                if child.tagName == 'style:page-layout-properties':
                    for prop in child.childNodes:
                        if prop.tagName == 'style:background-image':
                            print(f"        HREF Old: {prop.attributes[('http://www.w3.org/1999/xlink', 'href')]}")
                            prop.attributes[('http://www.w3.org/1999/xlink', 'href')] = png_name
                            print(f"        HREF New: {prop.attributes[('http://www.w3.org/1999/xlink', 'href')]}")

    textdoc.save('./output/' + odt_name)
