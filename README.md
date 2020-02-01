# notepad

PF Internet to File for Graduate Students

Goals:
• Write a Python 3 Tkinter GUI program with a simple interface with some buttons and fields to enter keywords for processing.
• Get data from the Internet using Python 3 features we discussed in class
• Reading more complex formats than text using the Python 3 features discussed in class (if
you use text, maximum grade is B).
• Processing data in your files using Python 3 features we discussed in class
• No other libraries or resources can be used.

These are the features your Python 3 script should do for a grade of B or better:
• Internet Access
o Access a website, email server, or other online source and pull data from it. o The data you download can be anything that you think will be interesting.
▪ If you can’t think of anything, select a website and get the .html, JSON or XML data from the main page. I showed you how to do this and we did it in class.
▪ Another simple idea is to get the data on emails received from your website using python3.
• Then your program can pick only to, only from, only subject based on user input.
• We have done this in class, so again, this will earn a B at best. o Save the raw, unprocessed data you downloaded on your hard drive as a file.
▪ Make sure you know where it is saved and what it is called.
▪ It is best if it is saved to the project directory without having to add a path,
otherwise it’ll crash on my computer.
• Reading complex formats
o You can choose .html, XML, JSON from a website, .pdf, or another type we have
discussed. You can also use Word files if you know how to read them. o You can use the Python3 tools we have discussed to work with the files.
• Processing files
o Choose a subset of the data to process.
▪ Look for a specific tag/format info from the file.
▪ Sort it in alphabetical order using language functions. o Format the data as a report and output it to an output file.
▪ This can be a .csv, .txt format.
▪ .pdf or XML is also acceptable, use the correct extension for your file.



PF Internet to File for Graduate Students
•
GUI Development.
o Create pull-down menus from the menu bar like the example done in class. File, Edit, and Help.
o When the user selects open, have it open the file system dialog to select the downloaded file to open.
▪ Show the contents of the file on the screen.
▪ Have another button to sort the data,
▪ Have a text field (edit) to allow your user to enter a search word to find or
keyword to filter the data on the screen.
▪ Display the results of each operation on screen.
o Once the user has the data they want on screen, they can use Save from the file menu to put the selected data/processed data on screen into the output file.
▪ When user selects save, again open a dialog to select the file to write into, should also be a .txt file, but if you prefer to create a .csv or other type file from your data, go ahead.
▪ Save the data and return to the screen.
▪ The saved data should still be on the screen.
This needs to be 6 -8 hours of work for a good student. The sample code I made took a couple of hours.
• •
Challenges/options – impress me:
1. If your program has the basic features of a GUI interface that includes data entry and buttons, works with internet data and reads/writes files of complex types you can make it do whatever you think is interesting. Up to +2 points
Testing, Documentation, and Submission.
• Run your program using several test cases (enough to test all parts of the program). Copy the output and put it all into one file. Label each test clearly with a clear description. Add your own test cases to the end. If the source website not found/retrieval fails, the program must still end gracefully. Copy and save the input and output from each run as run1in.csv and run1out.txt (or whatever extension is correct).
Label the console output for test 1 like this:
+++++++++++++ Test 1 – source website is not found/retrieval fails +++++++++++
Test the program at least three times,

CSCI 6651 Python Programming Final Exam Question
PF Internet to File for Graduate Students
1. Test one: the source website is not found/retrieval fails.
2. Test two: everything goes as expected, data is successfully retrieved, processed,
and output.
3. Test three: change the processing criteria to cover another alternative.
4. Add as many test cases as you need to make sure that every line of code is
executed at least once.
