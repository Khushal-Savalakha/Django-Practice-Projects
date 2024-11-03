# Page Visit Counter with Django and Cookies

This repository demonstrates how to track page visits for individual users in Django using cookies. The project displays the total number of times a user has visited the page.

## How It Works

When a user visits the page, a cookie named `count` is created (or updated) to store the number of times they've accessed it. Each time the page is refreshed or revisited, the cookie is read, incremented, and displayed on the page.

### Code Structure

- **Template**: `counter.html` - Displays the visit count.
- **View**: `page_count_view` - Handles the logic for reading, updating, and setting the cookie.

### Code Explanation

1. **View Function**: `page_count_view`

   ```python
   from django.shortcuts import render

   def page_count_view(request):
       count = int(request.COOKIES.get('count', 0))  # Retrieve 'count' cookie or default to 0
       count += 1                                   # Increment the count
       response = render(request, 'testapp/counter.html', {'count': count})  # Render response with count
       response.set_cookie('count', count)          # Set/update the 'count' cookie with new value
       return response                             # Return the response
   ```

2. **Template**: `counter.html`

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Page Visit Counter</title>
   </head>
   <body>
       <h1>Page Count: {{ count }}</h1>
   </body>
   </html>
   ```

### Example Flow

1. **First Visit**:
   - When the user first visits the page, there’s no `count` cookie yet.
   - The view initializes `count` to `0`, increments it to `1`, and sends `count=1` back in the response as a cookie.
   
   **Response**:
   ```http
   Set-Cookie: count=1
   ```
   ![First Visit](https://github.com/user-attachments/assets/476d6084-13bb-4779-a984-219fadeceddf)

2. **Subsequent Visits**:
   - On each visit, the browser sends the `count` cookie along with the request.
   - The view retrieves the cookie, increments its value by 1, and updates the `count` cookie in the response.
   
   **Example Request and Response**:
   ```http
   # Request Headers (sent by the client)
   Cookie: count=1
   
   # Response Headers (sent by the server)
   Set-Cookie: count=2
   ```
   ![Subsequent Visit](https://github.com/user-attachments/assets/445dc35b-d1fc-4b55-a934-e13b50dd9762)

### Visual Representation of the Flow

Here’s a visual representation of the flow from the client to the server and back, showing how the count is updated on each visit.

![Cookie Flow](https://github.com/user-attachments/assets/059c226c-c9e9-4de1-8423-acc70df01183)

### Video Demonstration
https://github.com/user-attachments/assets/476d6084-13bb-4779-a984-219fadeceddf


### Running the Project

1. **Set up Django environment**.
2. Add this view and template to your Django app.
3. Navigate to the view URL in the browser to see the visit count update.

### License

MIT License

