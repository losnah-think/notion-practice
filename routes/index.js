const Client = require("@notionhq/client");
require("dotenv").config();

const notion = new Client({ auth: process.env.NOTION_KEY })
const databaseId = process.env.NOTION_DATABASE_ID


var express = require('express');
var router = express.Router();

async function addItem(text) {
  try {
    await notion.request({
      path: "pages",
      method: "POST",
      body: {
        parent: { database_id: databaseId },
        properties: {
          title: { 
            title:[
              {
                "text": {
                  "content": text
                }
              }
            ]
          }
        }
      },
    })
    console.log("Success! Entry added.")
  } catch (error) {
    console.error(error.body)
  }
}

addItem("Yurts in Big Sur, California")

module.exports = router;
