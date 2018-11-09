**Install**




**Run application:**
python manage.py runserver

**Usage:**

Available Endponits:

- GET /   
    Download main page html
- GET /detail/\<str:alias>\<int:globalId>       
    Download detail html
    > alias - quest alias    
     globalId - quest globalId
   
- POST /api/        
    Upload FinishedQuestsLeafs.json     
    > Body: \<File content>




   
   
      