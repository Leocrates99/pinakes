# Genera un codice a barre EAN-13 pulito per testare la decodifica. (file di test, non parte dell'app)
from PIL import Image, ImageDraw
L={'0':'0001101','1':'0011001','2':'0010011','3':'0111101','4':'0100011','5':'0110001','6':'0101111','7':'0111011','8':'0110111','9':'0001011'}
G={'0':'0100111','1':'0110011','2':'0011011','3':'0100001','4':'0011101','5':'0111001','6':'0000101','7':'0010001','8':'0001001','9':'0010111'}
R={'0':'1110010','1':'1100110','2':'1101100','3':'1000010','4':'1011100','5':'1001110','6':'1010000','7':'1000100','8':'1001000','9':'1110100'}
PAR={'0':'LLLLLL','1':'LLGLGG','2':'LLGGLG','3':'LLGGGL','4':'LGLLGG','5':'LGGLLG','6':'LGGGLL','7':'LGLGLG','8':'LGLGGL','9':'LGGLGL'}

def ean13_bits(code):
    first=code[0]; left=code[1:7]; right=code[7:13]; par=PAR[first]
    bits='101'
    for d,p in zip(left,par): bits+= (L[d] if p=='L' else G[d])
    bits+='01010'
    for d in right: bits+=R[d]
    bits+='101'
    return bits

def render(code, mod=4, height=240, quiet=12, path='barcode_test.png'):
    bits=ean13_bits(code)
    w=(len(bits)+2*quiet)*mod
    img=Image.new('RGB',(w,height+40),'white')
    d=ImageDraw.Draw(img)
    x=quiet*mod
    for b in bits:
        if b=='1': d.rectangle([x,10,x+mod-1,height],fill='black')
        x+=mod
    img.save(path)
    print('Salvato',path,img.size,'EAN-13',code)

code='9783161484100'
assert len(code)==13
render(code, path=r'C:\Users\fasci\Downloads\Pinakes\barcode_test.png')
