"""Build a styled pandoc reference.docx (fonts, heading colors, callout and lead styles, table look)."""
import re, sys, zipfile, shutil, os

src, out = sys.argv[1], sys.argv[2]
NAVY, GREEN, RUST, SHADE = "1B2A41", "2E6F57", "9A4A1C", "EEF4F0"
HEAD, BODY = "Georgia", "Calibri"

z = zipfile.ZipFile(src)
files = {n: z.read(n) for n in z.namelist()}
s = files["word/styles.xml"].decode()

def replace_style(sid, xml):
    global s
    s = re.sub(r'<w:style [^>]*w:styleId="%s".*?</w:style>' % sid, xml, s, count=1, flags=re.S)

def rfonts(f):
    return f'<w:rFonts w:ascii="{f}" w:hAnsi="{f}" w:eastAsia="{f}" w:cs="{f}"/>'

s = re.sub(r'<w:docDefaults>.*?</w:docDefaults>',
    f'<w:docDefaults><w:rPrDefault><w:rPr>{rfonts(BODY)}<w:sz w:val="22"/><w:szCs w:val="22"/>'
    '<w:lang w:val="en-US" w:eastAsia="en-US" w:bidi="ar-SA"/></w:rPr></w:rPrDefault>'
    '<w:pPrDefault><w:pPr><w:spacing w:after="120" w:line="276" w:lineRule="auto"/></w:pPr></w:pPrDefault></w:docDefaults>',
    s, flags=re.S)

replace_style("BodyText", '<w:style w:type="paragraph" w:styleId="BodyText"><w:name w:val="Body Text"/><w:basedOn w:val="Normal"/>'
    '<w:link w:val="BodyTextChar"/><w:pPr><w:spacing w:before="100" w:after="120"/></w:pPr><w:qFormat/></w:style>')

def heading(n, size, color, before, after, caps=False, border=False):
    b = (f'<w:pBdr><w:bottom w:val="single" w:sz="6" w:space="4" w:color="{color}"/></w:pBdr>' if border else '')
    c = '<w:caps/>' if caps else ''
    return (f'<w:style w:type="paragraph" w:styleId="Heading{n}"><w:name w:val="heading {n}"/><w:basedOn w:val="Normal"/>'
            f'<w:next w:val="BodyText"/><w:uiPriority w:val="9"/><w:qFormat/><w:pPr><w:keepNext/><w:keepLines/>{b}'
            f'<w:spacing w:before="{before}" w:after="{after}"/><w:outlineLvl w:val="{n-1}"/></w:pPr>'
            f'<w:rPr>{rfonts(HEAD)}<w:b/><w:bCs/>{c}<w:color w:val="{color}"/><w:sz w:val="{size}"/><w:szCs w:val="{size}"/></w:rPr></w:style>')

replace_style("Heading1", heading(1, 34, NAVY, 360, 160, border=True))
replace_style("Heading2", heading(2, 26, GREEN, 280, 100))
replace_style("Heading3", heading(3, 22, RUST, 200, 60))

replace_style("Title", f'<w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:basedOn w:val="Normal"/>'
    f'<w:next w:val="BodyText"/><w:qFormat/><w:pPr><w:keepNext/><w:spacing w:before="0" w:after="80"/></w:pPr>'
    f'<w:rPr>{rfonts(HEAD)}<w:b/><w:color w:val="{NAVY}"/><w:sz w:val="52"/><w:szCs w:val="52"/></w:rPr></w:style>')
replace_style("Subtitle", f'<w:style w:type="paragraph" w:styleId="Subtitle"><w:name w:val="Subtitle"/><w:basedOn w:val="Normal"/>'
    f'<w:next w:val="BodyText"/><w:qFormat/><w:pPr><w:spacing w:before="0" w:after="240"/>'
    f'<w:pBdr><w:bottom w:val="single" w:sz="8" w:space="8" w:color="{GREEN}"/></w:pBdr></w:pPr>'
    f'<w:rPr>{rfonts(HEAD)}<w:i/><w:color w:val="{GREEN}"/><w:sz w:val="26"/><w:szCs w:val="26"/></w:rPr></w:style>')

extra = (
  f'<w:style w:type="paragraph" w:customStyle="1" w:styleId="Callout"><w:name w:val="Callout"/><w:basedOn w:val="BodyText"/><w:qFormat/>'
  f'<w:pPr><w:pBdr><w:top w:val="single" w:sz="6" w:space="6" w:color="{GREEN}"/><w:left w:val="single" w:sz="6" w:space="6" w:color="{GREEN}"/>'
  f'<w:bottom w:val="single" w:sz="6" w:space="6" w:color="{GREEN}"/><w:right w:val="single" w:sz="6" w:space="6" w:color="{GREEN}"/></w:pBdr>'
  f'<w:shd w:val="clear" w:color="auto" w:fill="{SHADE}"/><w:spacing w:before="160" w:after="160"/><w:ind w:left="144" w:right="144"/></w:pPr></w:style>'
  f'<w:style w:type="paragraph" w:customStyle="1" w:styleId="Warning"><w:name w:val="Warning"/><w:basedOn w:val="BodyText"/><w:qFormat/>'
  f'<w:pPr><w:pBdr><w:top w:val="single" w:sz="6" w:space="6" w:color="{RUST}"/><w:left w:val="single" w:sz="6" w:space="6" w:color="{RUST}"/>'
  f'<w:bottom w:val="single" w:sz="6" w:space="6" w:color="{RUST}"/><w:right w:val="single" w:sz="6" w:space="6" w:color="{RUST}"/></w:pBdr>'
  f'<w:shd w:val="clear" w:color="auto" w:fill="FBF1EA"/><w:spacing w:before="160" w:after="160"/><w:ind w:left="144" w:right="144"/></w:pPr></w:style>'
  f'<w:style w:type="paragraph" w:customStyle="1" w:styleId="Lead"><w:name w:val="Lead"/><w:basedOn w:val="BodyText"/><w:qFormat/>'
  f'<w:pPr><w:spacing w:before="120" w:after="200"/></w:pPr><w:rPr><w:color w:val="404040"/><w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr></w:style>'
  f'<w:style w:type="paragraph" w:customStyle="1" w:styleId="Formula"><w:name w:val="Formula"/><w:basedOn w:val="BodyText"/><w:qFormat/>'
  f'<w:pPr><w:shd w:val="clear" w:color="auto" w:fill="F4F6FA"/><w:spacing w:before="80" w:after="80"/><w:ind w:left="360" w:right="360"/><w:jc w:val="center"/></w:pPr>'
  f'<w:rPr><w:b/><w:color w:val="{NAVY}"/></w:rPr></w:style>'
)
s = s.replace('</w:styles>', extra + '</w:styles>')

# Table look: light grid, navy header row with white bold text
replace_style("Table", f'<w:style w:type="table" w:default="1" w:styleId="Table"><w:name w:val="Table"/><w:basedOn w:val="TableNormal"/><w:qFormat/>'
  '<w:pPr><w:spacing w:before="40" w:after="40"/></w:pPr><w:rPr><w:sz w:val="20"/><w:szCs w:val="20"/></w:rPr>'
  '<w:tblPr><w:tblInd w:w="0" w:type="dxa"/><w:tblBorders>'
  '<w:top w:val="single" w:sz="4" w:color="B7C3BD"/><w:left w:val="single" w:sz="4" w:color="B7C3BD"/>'
  '<w:bottom w:val="single" w:sz="4" w:color="B7C3BD"/><w:right w:val="single" w:sz="4" w:color="B7C3BD"/>'
  '<w:insideH w:val="single" w:sz="4" w:color="B7C3BD"/><w:insideV w:val="single" w:sz="4" w:color="B7C3BD"/></w:tblBorders>'
  '<w:tblCellMar><w:top w:w="40" w:type="dxa"/><w:left w:w="100" w:type="dxa"/><w:bottom w:w="40" w:type="dxa"/><w:right w:w="100" w:type="dxa"/></w:tblCellMar></w:tblPr>'
  f'<w:tblStylePr w:type="firstRow"><w:rPr><w:b/><w:color w:val="FFFFFF"/></w:rPr><w:tcPr><w:shd w:val="clear" w:color="auto" w:fill="{NAVY}"/><w:vAlign w:val="bottom"/></w:tcPr></w:tblStylePr>'
  '</w:style>')

files["word/styles.xml"] = s.encode()

# US Letter, 1" margins
d = files["word/document.xml"].decode()
d = re.sub(r'<w:sectPr\s*/>|<w:sectPr>.*?</w:sectPr>', '<w:sectPr><w:pgSz w:w="12240" w:h="15840"/><w:pgMar w:top="1260" w:right="1260" w:bottom="1260" w:left="1260" w:header="720" w:footer="720" w:gutter="0"/></w:sectPr>', d, flags=re.S)
files["word/document.xml"] = d.encode()


# Footer with centered page number
footer = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
  '<w:ftr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
  'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
  '<w:p><w:pPr><w:jc w:val="center"/></w:pPr>'
  '<w:r><w:rPr><w:color w:val="7F7F7F"/><w:sz w:val="18"/></w:rPr><w:fldChar w:fldCharType="begin"/></w:r>'
  '<w:r><w:rPr><w:color w:val="7F7F7F"/><w:sz w:val="18"/></w:rPr><w:instrText xml:space="preserve"> PAGE </w:instrText></w:r>'
  '<w:r><w:rPr><w:color w:val="7F7F7F"/><w:sz w:val="18"/></w:rPr><w:fldChar w:fldCharType="separate"/></w:r>'
  '<w:r><w:rPr><w:color w:val="7F7F7F"/><w:sz w:val="18"/></w:rPr><w:t>1</w:t></w:r>'
  '<w:r><w:rPr><w:color w:val="7F7F7F"/><w:sz w:val="18"/></w:rPr><w:fldChar w:fldCharType="end"/></w:r>'
  '</w:p></w:ftr>')
files["word/footer1.xml"] = footer.encode()
rels = files["word/_rels/document.xml.rels"].decode()
if 'footer1.xml' not in rels:
    rels = rels.replace('</Relationships>', '<Relationship Id="rIdFooter1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/></Relationships>')
files["word/_rels/document.xml.rels"] = rels.encode()
ct = files["[Content_Types].xml"].decode()
if 'footer1.xml' not in ct:
    ct = ct.replace('</Types>', '<Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/></Types>')
files["[Content_Types].xml"] = ct.encode()
d = files["word/document.xml"].decode()
d = d.replace('<w:sectPr><w:pgSz', '<w:sectPr><w:footerReference w:type="default" r:id="rIdFooter1"/><w:pgSz')
if 'xmlns:r=' not in d[:2000]:
    d = d.replace('<w:document ', '<w:document xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" ', 1)
files["word/document.xml"] = d.encode()

with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as o:
    for n, b in files.items():
        o.writestr(n, b)
print("wrote", out)
