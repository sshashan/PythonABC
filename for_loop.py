"*********FOR LOOP EXAMPLE******"
blog_posts=["Hi All,","","My Name is Sujay Shashank","","I am from Ranchi."]
for post in blog_posts:
      if(post !=""):
            print(post)
      else:
            continue

      
blog_posts1={"Sujay":["Hi All","My Name is Sujay Shashank","I am from Ranchi."],"Titas":["My Name is Titas Datta","I am from Howrah"]}

for key in blog_posts1:
      print(key.upper())
      for data in blog_posts1[key]:
            print(data)
