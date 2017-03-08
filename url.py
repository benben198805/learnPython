from urllib import request
import json
import pydash
from pydash import *

req = request.Request('https://www.zhihu.com/api/v4/questions/22762170/answers?include=data%5B*%5D.is_normal%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccollapsed_counts%2Creviewing_comments_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Cmark_infos%2Ccreated_time%2Cupdated_time%2Crelationship.is_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B*%5D.author.is_blocking%2Cis_blocked%2Cis_followed%2Cvoteup_count%2Cmessage_thread_token%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=3&limit=20&sort_by=default')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('authorization','oauth c3cef7c66a1843f8b3a9e6a1e3160e20')


with request.urlopen(req) as f:
    response = f.read()
    print('Status:', f.status, f.reason)
    print('----------------------------')

    jsonData = json.loads(response)

    data = jsonData['data']

    l = chain(data).map(lambda item:{
            'auth':item['author']['name'],
            'voteup':item['voteup_count'],
            'excerpt':item['excerpt']
        }).sort_by('voteup', reverse=True).value()
    for item in l:
        print('auth:%s,voteup:%s'%(item['auth'], item['voteup']))
        print('content:%s\n'%item['excerpt'])
