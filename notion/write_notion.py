# os, os.path, dotenv 는 환경설정값을 저장해둔 env 파일 값을 불러오기 위함이다.
# notion.block 을 통해서 블록에 대한 모든 행위들을 할 수 있다.
import os
from notion.client import NotionClient
from notion.block import TodoBlock
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

# NotionClient는 노션 페이지지를 받아오기 위해 노션 v2 토큰을 받는다.
client = NotionClient(token_v2=os.environ.get("NOTION_TOKEN"))
# 토큰이 적용된 client 객체에서 블록 정보를 받아온다.
page = client.get_block(os.environ.get("NOTION_URL"))

### 원래는 정상적으로 추가가 되어야하는 내용인데... 에러가 난다..
newchild = page.children.add_new(TodoBlock, title="Something to get done")
newchild.checked = True