This is a simple Flask app for monitoring 
- Cpu usage
- RAM usage
- Free storage
from your browser (Flask)

pre-requisites:
- python3
- pip3

I used it to constantly monitor my test server while working on my finel project in college.

Remember that this will work only in your LAN

If you have the need to monitor other paramerters:
1.  Add the required fields to the `output.html` file:

   ```
   <div class="parameter">
       <h2><parameter name></h2>
       <p>{{ variable name }} MB</p>
   </div>
    ```

2. add a function to the app.py file
3. add it to the infinite loop in the app.py file
    variable name = function()
4. pass the variable to the output.html file through the render_template function

To run the app, run the following commands in the terminal:

$ pip install -r requirements.txt

$ python3 app.py
