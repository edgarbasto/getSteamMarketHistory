# Export Steam Market History to Excel
# Instructions

FYI: this is not tunned up. 
I only spend less than 30mins setting up this script to extract the info I needed. 
Prices are exported as a string, you have to convert in excel.
Maybe one day I'll improve it... (maybe not!)

1. Clone GIT to your local machine
2. Go to your steamcommunity Market history webpage
3. Open your browser console and type (max 100)  
   `g_oMyHistory.m_cPageSize = 100`
4. Do not refresh. Select a different page from history or type in console  
   `g_oMyHistory.GoToPage(1)` (will take you to second page)  
    You are free to navigate on the pages
5. Save each page (right click on the page) inside htmls directory  
    e.g. page1.html, page2.html... (make sure to use .html extension)
6. Run steammarkethistory.py
7. Open output.xlsx

The wallet history you can copy/past directly to excel.
