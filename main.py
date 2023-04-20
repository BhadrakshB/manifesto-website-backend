from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

server = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:8080",
    "http://localhost:59148"
]

server.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@server.get("/candidates")
async def root():
    return {
  "candidates": [
    {
      "name": "Rishik Nair","age": "19","position": "Vice President","manifesto": "I am madarchod"
    },
    {
      "name": "Bhadraksh Bhargava","age": "19","position": "Vice Technical Secretary","manifesto": "Gaand Marao sab"
    },
    {
      "name": "Yash Khaitan","age": "19","position": "Vice Cultural Secretary","manifesto": "Bhagwaan hu main"
    },
    {
      "name": "Rohith S. Bellur","age": "20","position": "Vice Sports Secretary","manifesto": "Sports mein best hain apun"
    },
    {
      "name": "Jagmohan Dixit","age": "21","position": "President","manifesto": "JOD HU MAIN"
    },
    {
      "name": "Kamal Raj","age": "21","position": "Sports Secretary","manifesto": "ENNA TEVDIYA"
    },
    {
      "name": "Gautam Dadhich","age": "21","position": "Technical Secretary","manifesto": "Madarchod Jaipur aajao sab"
    },
    {
      "name": "Cultural Secretary","age": "21","position": "Cultural Secretary","manifesto": "Chutiyo karwata hu Aahladh main betichodo"
    }
  ]
}

