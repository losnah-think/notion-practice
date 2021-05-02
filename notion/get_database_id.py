import os
import datetime
from os.path import join, dirname
from notion.client import NotionClient
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

client = NotionClient(token_v2=os.environ.get("NOTION_TOKEN"))
blog_home = client.get_block(os.environ.get("NOTION_URL"))

# Main Loop
for post in blog_home.children:
    # Handle Frontmatter
    text = """---
title: %s
date: "%s"
description: ""
---""" % (post.title, datetime.datetime.now())
    # Handle Title
    text = text + '\\n\\n' + '# ' + post.title + '\\n\\n'
    for block in post.children:
        # Handles H1
        if (block.type == 'header'):
            text = text + '# ' + block.title + '\\n\\n'
        # Handles H2
        if (block.type == 'sub_header'):
            text = text + '## ' + block.title + '\\n\\n'
        # Handles H3
        if (block.type == 'sub_sub_header'):
            text = text + '### ' + block.title + '\\n\\n'
        # Handles Code Blocks
        if (block.type == 'code'):
            text = text + '```\\n' + block.title + '\\n```\\n'
        # Handles Images
        if (block.type == 'image'):
            text = text + '![' + block.id + '](' + block.source + ')\\n\\n'
        # Handles Bullets
        if (block.type == 'bulleted_list'):
            text = text + '* ' + block.title + '\\n'
        # Handles Dividers
        if (block.type == 'divider'):
            text = text + '---' + '\\n'
        # Handles Basic Text, Links, Single Line Code
        if (block.type == 'text'):
            text = text + block.title + '\\n'
    title = post.title.replace(' ', '-')
    title = title.replace(',', '')
    title = title.replace(':', '')
    title = title.replace(';', '')
    title = title.lower()
    try:
        os.mkdir('../contents/blog/' + title)
    except:
        print("폴더 생성에 실패했습니다.")
        pass
    file = open('../contents/blog/' + title + '/index.mdx', 'w')
    print('Wrote A New Page')
    print(text)
    file.write(text)