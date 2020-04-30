# Initialize to None Google Material Colors names
gred050 = None
gred100 = None
gred200 = None
gred300 = None
gred400 = None
gred500 = None
gred600 = None
gred700 = None
gred800 = None
gred900 = None

gpink050 = None
gpink100 = None
gpink200 = None
gpink300 = None
gpink400 = None
gpink500 = None
gpink600 = None
gpink700 = None
gpink800 = None
gpink900 = None

gpurple050 = None
gpurple100 = None
gpurple200 = None
gpurple300 = None
gpurple400 = None
gpurple500 = None
gpurple600 = None
gpurple700 = None
gpurple800 = None
gpurple900 = None

gdpurple050 = None
gdpurple100 = None
gdpurple200 = None
gdpurple300 = None
gdpurple400 = None
gdpurple500 = None
gdpurple600 = None
gdpurple700 = None
gdpurple800 = None
gdpurple900 = None

gindigo050 = None
gindigo100 = None
gindigo200 = None
gindigo300 = None
gindigo400 = None
gindigo500 = None
gindigo600 = None
gindigo700 = None
gindigo800 = None
gindigo900 = None

gblue050 = None
gblue100 = None
gblue200 = None
gblue300 = None
gblue400 = None
gblue500 = None
gblue600 = None
gblue700 = None
gblue800 = None
gblue900 = None

glblue050 = None
glblue100 = None
glblue200 = None
glblue300 = None
glblue400 = None
glblue500 = None
glblue600 = None
glblue700 = None
glblue800 = None
glblue900 = None

gcyan050 = None
gcyan100 = None
gcyan200 = None
gcyan300 = None
gcyan400 = None
gcyan500 = None
gcyan600 = None
gcyan700 = None
gcyan800 = None
gcyan900 = None

gteal050 = None
gteal100 = None
gteal200 = None
gteal300 = None
gteal400 = None
gteal500 = None
gteal600 = None
gteal700 = None
gteal800 = None
gteal900 = None

ggreen050 = None
ggreen100 = None
ggreen200 = None
ggreen300 = None
ggreen400 = None
ggreen500 = None
ggreen600 = None
ggreen700 = None
ggreen800 = None
ggreen900 = None

glgreen050 = None
glgreen100 = None
glgreen200 = None
glgreen300 = None
glgreen400 = None
glgreen500 = None
glgreen600 = None
glgreen700 = None
glgreen800 = None
glgreen900 = None

glime050 = None
glime100 = None
glime200 = None
glime300 = None
glime400 = None
glime500 = None
glime600 = None
glime700 = None
glime800 = None
glime900 = None

gyellow050 = None
gyellow100 = None
gyellow200 = None
gyellow300 = None
gyellow400 = None
gyellow500 = None
gyellow600 = None
gyellow700 = None
gyellow800 = None
gyellow900 = None

gamber050 = None
gamber100 = None
gamber200 = None
gamber300 = None
gamber400 = None
gamber500 = None
gamber600 = None
gamber700 = None
gamber800 = None
gamber900 = None

gorange050 = None
gorange100 = None
gorange200 = None
gorange300 = None
gorange400 = None
gorange500 = None
gorange600 = None
gorange700 = None
gorange800 = None
gorange900 = None

gdorange050 = None
gdorange100 = None
gdorange200 = None
gdorange300 = None
gdorange400 = None
gdorange500 = None
gdorange600 = None
gdorange700 = None
gdorange800 = None
gdorange900 = None

gbrown050 = None
gbrown100 = None
gbrown200 = None
gbrown300 = None
gbrown400 = None
gbrown500 = None
gbrown600 = None
gbrown700 = None
gbrown800 = None
gbrown900 = None

gbgrey050 = None
gbgrey100 = None
gbgrey200 = None
gbgrey300 = None
gbgrey400 = None
gbgrey500 = None
gbgrey600 = None
gbgrey700 = None
gbgrey800 = None
gbgrey900 = None

ggrey050 = None
ggrey100 = None
ggrey200 = None
ggrey300 = None
ggrey400 = None
ggrey500 = None
ggrey600 = None
ggrey700 = None
ggrey800 = None
ggrey900 = None

gblack = None
gwhite = None

def SetGMaterialColors():
    """
    Name: SetGMaterialColors.
    
    by Carlos Mario Granados Castro, 2013-2019
    
    Description : Function to set the Google Material Design Color set. It
    only includes primary shades, from 050 to 900. For more information
    see https://material.io/design/color/the-color-system.html#tools-for-picking-colors
    
    Import as: import ModColors as gc
               gc.SetGMaterialColors()
    
    Each color is called as: gc.g[colorName][Shade].
    Ex: for red is gc.gred500 or gc.gred700
    
    Color Names: red, pink, purple, indigo, blue, lblue, cyan, teal, green, lgreen,
                 lime, yellow, amber, orange, dorange, bgrey, grey. <black>, <white> 
    """
    global gred050, gred100, gred200, gred300, gred400, gred500, gred600, gred700, gred800, gred900
    global gpink050, gpink100, gpink200, gpink300, gpink400, gpink500, gpink600, gpink700, gpink800, gpink900
    global gpurple050, gpurple100, gpurple200, gpurple300, gpurple400, gpurple500, gpurple600, gpurple700, gpurple800, gpurple900
    global gdpurple050, gdpurple100, gdpurple200, gdpurple300, gdpurple400, gdpurple500, gdpurple600, gdpurple700, gdpurple800, gdpurple900
    global gindigo050, gindigo100, gindigo200, gindigo300, gindigo400, gindigo500, gindigo600, gindigo700, gindigo800, gindigo900
    global gblue050, gblue100, gblue200, gblue300, gblue400, gblue500, gblue600, gblue700, gblue800, gblue900
    global glblue050, glblue100, glblue200, glblue300, glblue400, glblue500, glblue600, glblue700, glblue800, glblue900
    global gcyan050, gcyan100, gcyan200, gcyan300, gcyan400, gcyan500, gcyan600, gcyan700, gcyan800, gcyan900
    global gteal050, gteal100, gteal200, gteal300, gteal400, gteal500, gteal600, gteal700, gteal800, gteal900
    global ggreen050, ggreen100, ggreen200, ggreen300, ggreen400, ggreen500, ggreen600, ggreen700, ggreen800, ggreen900
    global glgreen050, glgreen100, glgreen200, glgreen300, glgreen400, glgreen500, glgreen600, glgreen700, glgreen800, glgreen900
    global glime050, glime100, glime200, glime300, glime400, glime500, glime600, glime700, glime800, glime900
    global gyellow050, gyellow100, gyellow200, gyellow300, gyellow400, gyellow500, gyellow600, gyellow700, gyellow800, gyellow900
    global gamber050, gamber100, gamber200, gamber300, gamber400, gamber500, gamber600, gamber700, gamber800, gamber900
    global gorange050, gorange100, gorange200, gorange300, gorange400, gorange500, gorange600, gorange700, gorange800, gorange900
    global gdorange050, gdorange100, gdorange200, gdorange300, gdorange400, gdorange500, gdorange600, gdorange700, gdorange800, gdorange900
    global gbrown050, gbrown100, gbrown200, gbrown300, gbrown400, gbrown500, gbrown600, gbrown700, gbrown800, gbrown900
    global gbgrey050, gbgrey100, gbgrey200, gbgrey300, gbgrey400, gbgrey500, gbgrey600, gbgrey700, gbgrey800, gbgrey900
    global ggrey050, ggrey100, ggrey200, ggrey300, ggrey400, ggrey500, ggrey600, ggrey700, ggrey800, ggrey900
    global gblack, gwhite
    gred050 = '#FFEBEE'
    gred100 = '#FFCDD2'
    gred200 = '#EF9A9A'
    gred300 = '#E57373'
    gred400 = '#EF5350'
    gred500 = '#F44336'
    gred600 = '#E53935'
    gred700 = '#D32F2F'
    gred800 = '#C62828'
    gred900 = '#B71C1C'
    gpink050 = '#FCE4EC'
    gpink100 = '#F8BBD0'
    gpink200 = '#F48FB1'
    gpink300 = '#F06292'
    gpink400 = '#EC407A'
    gpink500 = '#E91E63'
    gpink600 = '#D81B60'
    gpink700 = '#C2185B'
    gpink800 = '#AD1457'
    gpink900 = '#880E4F'
    gpurple050 = '#F3E5F5'
    gpurple100 = '#E1BEE7'
    gpurple200 = '#CE93D8'
    gpurple300 = '#BA68C8'
    gpurple400 = '#AB47BC'
    gpurple500 = '#9C27B0'
    gpurple600 = '#8E24AA'
    gpurple700 = '#7B1FA2'
    gpurple800 = '#6A1B9A'
    gpurple900 = '#4A148C'
    gdpurple050 = '#EDE7F6'
    gdpurple100 = '#D1C4E9'
    gdpurple200 = '#B39DDB'
    gdpurple300 = '#9575CD'
    gdpurple400 = '#7E57C2'
    gdpurple500 = '#673AB7'
    gdpurple600 = '#5E35B1'
    gdpurple700 = '#512DA8'
    gdpurple800 = '#4527A0'
    gdpurple900 = '#311B92'
    gindigo050 = '#E8EAF6'
    gindigo100 = '#C5CAE9'
    gindigo200 = '#9FA8DA'
    gindigo300 = '#7986CB'
    gindigo400 = '#5C6BC0'
    gindigo500 = '#3F51B5'
    gindigo600 = '#3949AB'
    gindigo700 = '#303F9F'
    gindigo800 = '#283593'
    gindigo900 = '#1A237E'
    gblue050 = '#E3F2FD'
    gblue100 = '#BBDEFB'
    gblue200 = '#90CAF9'
    gblue300 = '#64B5F6'
    gblue400 = '#42A5F5'
    gblue500 = '#2196F3'
    gblue600 = '#1E88E5'
    gblue700 = '#1976D2'
    gblue800 = '#1565C0'
    gblue900 = '#0D47A1'
    glblue050 = '#E1F5FE'
    glblue100 = '#B3E5FC'
    glblue200 = '#81D4FA'
    glblue300 = '#4FC3F7'
    glblue400 = '#29B6F6'
    glblue500 = '#03A9F4'
    glblue600 = '#039BE5'
    glblue700 = '#0288D1'
    glblue800 = '#0277BD'
    glblue900 = '#01579B'
    gcyan050 = '#E0F7FA'
    gcyan100 = '#B2EBF2'
    gcyan200 = '#80DEEA'
    gcyan300 = '#4DD0E1'
    gcyan400 = '#26C6DA'
    gcyan500 = '#00BCD4'
    gcyan600 = '#00ACC1'
    gcyan700 = '#0097A7'
    gcyan800 = '#00838F'
    gcyan900 = '#006064'
    gteal050 = '#E0F2F1'
    gteal100 = '#B2DFDB'
    gteal200 = '#80CBC4'
    gteal300 = '#4DB6AC'
    gteal400 = '#26A69A'
    gteal500 = '#009688'
    gteal600 = '#00897B'
    gteal700 = '#00796B'
    gteal800 = '#00695C'
    gteal900 = '#00AD40'
    ggreen050 = '#E8F5E9'
    ggreen100 = '#C8E6C9'
    ggreen200 = '#A5D6A7'
    ggreen300 = '#81C784'
    ggreen400 = '#66BB6A'
    ggreen500 = '#4CAF50'
    ggreen600 = '#43A047'
    ggreen700 = '#388E3C'
    ggreen800 = '#2E7D32'
    ggreen900 = '#1B5E20'
    glgreen050 = '#F1F8E9'
    glgreen100 = '#DCEDC8'
    glgreen200 = '#C5E1A5'
    glgreen300 = '#AED581'
    glgreen400 = '#9CCC65'
    glgreen500 = '#8BC34A'
    glgreen600 = '#7CB342'
    glgreen700 = '#689F38'
    glgreen800 = '#558B2F'
    glgreen900 = '#33691E'
    glime050 = '#F9FBE7'
    glime100 = '#F0F4C3'
    glime200 = '#E6EE9C'
    glime300 = '#DCE775'
    glime400 = '#D4E157'
    glime500 = '#CDDC39'
    glime600 = '#C0CA33'
    glime700 = '#AFB42B'
    glime800 = '#9E9D24'
    glime900 = '#827717'
    gyellow050 = '#FFFDE7'
    gyellow100 = '#FFF9C4'
    gyellow200 = '#FFF59D'
    gyellow300 = '#FFF176'
    gyellow400 = '#FFEE58'
    gyellow500 = '#FFEB3B'
    gyellow600 = '#FDD835'
    gyellow700 = '#FBC02D'
    gyellow800 = '#F9A825'
    gyellow900 = '#F57F17'
    gamber050 = '#FFF8E1'
    gamber100 = '#FFECB3'
    gamber200 ='#FFE082'
    gamber300 = '#FFD54F'
    gamber400 = '#FFCA28'
    gamber500 = '#FFC107'
    gamber600 = '#FFB300'
    gamber700 = '#FFA000'
    gamber800 = '#FF8F00'
    gamber900 = '#FF6F00'
    gorange050 = '#FFF3E0'
    gorange100 = '#FFE0B2'
    gorange200 = '#FFCC80'
    gorange300 = '#FFB74D'
    gorange400 = '#FFA726'
    gorange500 = '#FF9800'
    gorange600 = '#FB8C00'
    gorange700 = '#F57C00'
    gorange800 = '#EF6C00'
    gorange900 = '#E65100'
    gdorange050 = '#FBE9E7'
    gdorange100 = '#FFCCBC'
    gdorange200 = '#FFAB91'
    gdorange300 = '#FF8A65'
    gdorange400 = '#FF7043'
    gdorange500 = '#FF5722'
    gdorange600 = '#F4511E'
    gdorange700 = '#E64A19'
    gdorange800 = '#D84315'
    gdorange900 = '#BF360C'
    gbrown050 = '#EFEBE9'
    gbrown100 = '#D7CCC8'
    gbrown200 = '#BCAAA4'
    gbrown300 = '#A1887F'
    gbrown400 = '#8D6E63'
    gbrown500 = '#795548'
    gbrown600 = '#6D4C41'
    gbrown700 = '#5D4037'
    gbrown800 = '#4E342E'
    gbrown900 = '#3E2723'
    gbgrey050 = '#ECEFF1'
    gbgrey100 = '#CFD8DC'
    gbgrey200 = '#B0BEC5'
    gbgrey300 = '#90A4AE'
    gbgrey400 = '#78909C'
    gbgrey500 = '#607D8B'
    gbgrey600 = '#546E7A'
    gbgrey700 = '#455A64'
    gbgrey800 = '#37474F'
    gbgrey900 = '#263238'
    ggrey050 = '#FAFAFA'
    ggrey100 = '#F5F5F5'
    ggrey200 = '#EEEEEE'
    ggrey300 = '#E0E0E0'
    ggrey400 = '#BDBDBD'
    ggrey500 = '#9E9E9E'
    ggrey600 = '#757575'
    ggrey700 = '#616161'
    ggrey800 = '#424242'
    ggrey900 = '#212121'
    gblack = '#000000'
    gwhite = '#FFFFFF'

