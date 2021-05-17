import requests
import urllib.parse

# Template would be array of elements here.
# Each element starts with element type. e.g. type:value
# type here can be : heading,link,image,video
def update_feature(feature_id,name,template,token):
    print('Updating Feature : '+name)
    headers = {'authorization': 'Bearer '+token}
    html = ""
    for item in template:
        if item.startswith('heading:'):
            value = item.replace('heading:','')
            html += '<h2 style="text-align: center;">{}</h2>'.format(value)
        if item.startswith('link:'):
            value = item.replace('link:','')
            html += '''<div class="medium-insert-embeds" contenteditable="false">
                            <figure>
                                <div class="medium-insert-embed">
                                    <div data-embed-code="&lt;div class="iframely-embed"&gt;&lt;div class="iframely-responsive" style="padding-bottom: 52.5%; padding-top: 120px;"&gt;&lt;a href="{0}" data-iframely-url="//cdn.iframe.ly/api/iframe?url={1}&amp;amp;key=8a80ac46952afc453feb0074f16587ea"&gt;&lt;/a&gt;&lt;/div&gt;&lt;/div&gt;&lt;script async src="//cdn.iframe.ly/embed.js" charset="utf-8"&gt;&lt;/script&gt;"><div class="iframely-embed" style="max-width: 1442px;"><div class="iframely-responsive" style="padding-bottom: 0px; height: 496px;"><iframe allowfullscreen="" allow="autoplay *; encrypted-media *" src="//cdn.iframe.ly/api/iframe?url={1}&key=8a80ac46952afc453feb0074f16587ea&v=1&app=1" style="border: 1px solid rgb(222, 222, 222); box-shadow: rgba(0, 0, 0, 0.06) 0px 1px 3px;"></iframe></div></div><script async="" src="//cdn.iframe.ly/embed.js" charset="utf-8"></script></div>
                                </div>
                            </figure>
                            <div class="medium-insert-embeds-overlay"></div>
                        </div><p><br></p>'''.format(value,urllib.parse.quote(value,safe=''))
        if item.startswith('image:'):
            value = item.replace('image:','')
            html += '''<div class="medium-insert-images medium-insert-active">
                            <figure contenteditable="false">
		                        <img src="{}" alt="">
	                        </figure>
                        </div><p><br></p>'''.format(value)
        if item.startswith('video:'):
            value = item.replace('video:','')
            html += '''<div class="medium-insert-embeds" contenteditable="false">
                            <figure>
                                <div class="medium-insert-embed">
                                    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.25%;"><iframe src="{}" style="border: 0; top: 0; left: 0; width: 100%; height: 100%; position: absolute;" allowfullscreen="" scrolling="no" allow="encrypted-media; accelerometer; clipboard-write; gyroscope; picture-in-picture"></iframe></div>
                                </div>
                            </figure>
                            <div class="medium-insert-embeds-overlay"></div>
                        </div><p><br></p>'''.format(value)
    data = {
        "ID" : feature_id,
        "Html" : html,
        "Name" : name
    }
    r = requests.post('https://api.themap.net/api/Tour2/UpdateFeature', data = data, headers = headers)
    return r.json()
