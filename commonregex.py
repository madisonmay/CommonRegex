from types import MethodType
import re

date        = re.compile(u'(?:(?<!\:)(?<!\:\d)[0-3]?\d(?:st|nd|rd|th)?\s+(?:of\s+)?(?:jan\.?|january|feb\.?|february|mar\.?|march|apr\.?|april|may|jun\.?|june|jul\.?|july|aug\.?|august|sep\.?|september|oct\.?|october|nov\.?|november|dec\.?|december)|(?:jan\.?|january|feb\.?|february|mar\.?|march|apr\.?|april|may|jun\.?|june|jul\.?|july|aug\.?|august|sep\.?|september|oct\.?|october|nov\.?|november|dec\.?|december)\s+(?<!\:)(?<!\:\d)[0-3]?\d(?:st|nd|rd|th)?)(?:\,)?\s*(?:\d{4})?|[0-3]?\d[-\./][0-3]?\d[-\./]\d{2,4}', re.IGNORECASE)
time        = re.compile(u'\d{1,2}:\d{2} ?(?:[ap]\.?m\.?)?|\d[ap]\.?m\.?', re.IGNORECASE)
phone       = re.compile(u'((?:(?<![\d-])(?:\+?\d{1,3}[-.\s*]?)?(?:\(?\d{3}\)?[-.\s*]?)?\d{3}[-.\s*]?\d{4}(?![\d-]))|(?:(?<![\d-])(?:(?:\(\+?\d{2}\))|(?:\+?\d{2}))\s*\d{2}\s*\d{3}\s*\d{4}(?![\d-])))')
link        = re.compile(u'(?i)((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.](?:(?:ac)|(?:academy)|(?:ad)|(?:ae)|(?:aero)|(?:af)|(?:ag)|(?:agency)|(?:ai)|(?:al)|(?:am)|(?:an)|(?:ao)|(?:aq)|(?:ar)|(?:arpa)|(?:as)|(?:asia)|(?:at)|(?:au)|(?:aw)|(?:ax)|(?:az)|(?:ba)|(?:bb)|(?:bd)|(?:be)|(?:berlin)|(?:bf)|(?:bg)|(?:bh)|(?:bi)|(?:bike)|(?:biz)|(?:bj)|(?:bm)|(?:bn)|(?:bo)|(?:br)|(?:bs)|(?:bt)|(?:build)|(?:builders)|(?:buzz)|(?:bv)|(?:bw)|(?:by)|(?:bz)|(?:ca)|(?:cab)|(?:camera)|(?:camp)|(?:careers)|(?:cat)|(?:cc)|(?:cd)|(?:center)|(?:ceo)|(?:cf)|(?:cg)|(?:ch)|(?:cheap)|(?:ci)|(?:ck)|(?:cl)|(?:clothing)|(?:club)|(?:cm)|(?:cn)|(?:co)|(?:codes)|(?:coffee)|(?:com)|(?:company)|(?:computer)|(?:construction)|(?:contractors)|(?:coop)|(?:cr)|(?:cu)|(?:cv)|(?:cw)|(?:cx)|(?:cy)|(?:cz)|(?:dance)|(?:de)|(?:democrat)|(?:diamonds)|(?:directory)|(?:dj)|(?:dk)|(?:dm)|(?:do)|(?:domains)|(?:dz)|(?:ec)|(?:edu)|(?:education)|(?:ee)|(?:eg)|(?:email)|(?:enterprises)|(?:equipment)|(?:er)|(?:es)|(?:estate)|(?:et)|(?:eu)|(?:farm)|(?:fi)|(?:fj)|(?:fk)|(?:florist)|(?:fm)|(?:fo)|(?:fr)|(?:ga)|(?:gallery)|(?:gb)|(?:gd)|(?:ge)|(?:gf)|(?:gg)|(?:gh)|(?:gi)|(?:gift)|(?:gl)|(?:glass)|(?:gm)|(?:gn)|(?:gov)|(?:gp)|(?:gq)|(?:gr)|(?:graphics)|(?:gs)|(?:gt)|(?:gu)|(?:guitars)|(?:guru)|(?:gw)|(?:gy)|(?:hk)|(?:hm)|(?:hn)|(?:holdings)|(?:holiday)|(?:house)|(?:hr)|(?:ht)|(?:hu)|(?:id)|(?:ie)|(?:il)|(?:im)|(?:immobilien)|(?:in)|(?:info)|(?:institute)|(?:int)|(?:international)|(?:io)|(?:iq)|(?:ir)|(?:is)|(?:it)|(?:je)|(?:jm)|(?:jo)|(?:jobs)|(?:jp)|(?:kaufen)|(?:ke)|(?:kg)|(?:kh)|(?:ki)|(?:kitchen)|(?:kiwi)|(?:km)|(?:kn)|(?:kp)|(?:kr)|(?:kw)|(?:ky)|(?:kz)|(?:la)|(?:land)|(?:lb)|(?:lc)|(?:li)|(?:lighting)|(?:limo)|(?:link)|(?:lk)|(?:lr)|(?:ls)|(?:lt)|(?:lu)|(?:luxury)|(?:lv)|(?:ly)|(?:ma)|(?:management)|(?:marketing)|(?:mc)|(?:md)|(?:me)|(?:menu)|(?:mg)|(?:mh)|(?:mil)|(?:mk)|(?:ml)|(?:mm)|(?:mn)|(?:mo)|(?:mobi)|(?:moda)|(?:monash)|(?:mp)|(?:mq)|(?:mr)|(?:ms)|(?:mt)|(?:mu)|(?:museum)|(?:mv)|(?:mw)|(?:mx)|(?:my)|(?:mz)|(?:na)|(?:name)|(?:nc)|(?:ne)|(?:net)|(?:nf)|(?:ng)|(?:ni)|(?:ninja)|(?:nl)|(?:no)|(?:np)|(?:nr)|(?:nu)|(?:nz)|(?:om)|(?:onl)|(?:org)|(?:pa)|(?:pe)|(?:pf)|(?:pg)|(?:ph)|(?:photo)|(?:photography)|(?:photos)|(?:pics)|(?:pink)|(?:pk)|(?:pl)|(?:plumbing)|(?:pm)|(?:pn)|(?:post)|(?:pr)|(?:pro)|(?:ps)|(?:pt)|(?:pw)|(?:py)|(?:qa)|(?:re)|(?:recipes)|(?:red)|(?:repair)|(?:rich)|(?:ro)|(?:rs)|(?:ru)|(?:ruhr)|(?:rw)|(?:sa)|(?:sb)|(?:sc)|(?:sd)|(?:se)|(?:sexy)|(?:sg)|(?:sh)|(?:shiksha)|(?:shoes)|(?:si)|(?:singles)|(?:sj)|(?:sk)|(?:sl)|(?:sm)|(?:sn)|(?:so)|(?:social)|(?:solar)|(?:solutions)|(?:sr)|(?:st)|(?:su)|(?:support)|(?:sv)|(?:sx)|(?:sy)|(?:systems)|(?:sz)|(?:tattoo)|(?:tc)|(?:td)|(?:technology)|(?:tel)|(?:tf)|(?:tg)|(?:th)|(?:tips)|(?:tj)|(?:tk)|(?:tl)|(?:tm)|(?:tn)|(?:to)|(?:today)|(?:tp)|(?:tr)|(?:training)|(?:travel)|(?:tt)|(?:tv)|(?:tw)|(?:tz)|(?:ua)|(?:ug)|(?:uk)|(?:uno)|(?:us)|(?:uy)|(?:uz)|(?:va)|(?:vc)|(?:ve)|(?:ventures)|(?:vg)|(?:vi)|(?:viajes)|(?:vn)|(?:voyage)|(?:vu)|(?:wang)|(?:wf)|(?:wien)|(?:ws))/)(?:[^\s()<>]+[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019]))', re.IGNORECASE)
email       = re.compile(u"([a-z0-9!#$%&'*+\/=?^_`{|.}~-]+@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)", re.IGNORECASE)
ip          = re.compile(u'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)', re.IGNORECASE)
ipv6        = re.compile(u'\s*(?!.*::.*::)(?:(?!:)|:(?=:))(?:[0-9a-f]{0,4}(?:(?<=::)|(?<!::):)){6}(?:[0-9a-f]{0,4}(?:(?<=::)|(?<!::):)[0-9a-f]{0,4}(?:(?<=::)|(?<!:)|(?<=:)(?<!::):)|(?:25[0-4]|2[0-4]\d|1\d\d|[1-9]?\d)(?:\.(?:25[0-4]|2[0-4]\d|1\d\d|[1-9]?\d)){3})\s*', re.VERBOSE|re.IGNORECASE|re.DOTALL)
price       = re.compile(u'\$\s?[+-]?[0-9]{1,3}(?:,?[0-9])*(?:\.[0-9]{1,2})?')
hex_color   = re.compile(u'(#(?:[0-9a-fA-F]{8})|#(?:[0-9a-fA-F]{3}){1,2})\\b')
credit_card = re.compile(u'((?:(?:\\d{4}[- ]?){3}\\d{4}|\\d{16}))(?![\\d])')

regexes = {"dates"        : date,
           "times"        : time, 
           "phones"       : phone,
           "links"        : link,
           "emails"       : email,
           "ips"          : ip,
           "ipv6s"        : ipv6,
           "prices"       : price,
           "hex_colors"   : hex_color,
           "credit_cards" : credit_card}

class regex:

  def __init__(self, obj, regex):
    self.obj = obj
    self.regex = regex

  def __call__(self, *args):
    def regex_method(text=None):
      return [x.strip() for x in self.regex.findall(text or self.obj.text)]
    return regex_method

class CommonRegex(object):

    def __init__(self, text=""):
        self.text = text

        for k, v in regexes.items():
          setattr(self, k, regex(self, v)(self))

        if text:
            for key in regexes.keys():
                method = getattr(self, key)
                setattr(self, key, method())
