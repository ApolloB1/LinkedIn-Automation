from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display
import time, getpass

username = 'hassansaad0x@gmail.com' # username
password = 'inthenameofgod$A00' # password
visible = 0 # make the process unvisible, { visible = 1, unvisible = 0 }

if username == '':
  username = raw_input('Enter Username: ')

if password == '':
  password = getpass.getpass('Enter Password: ')


if visible == 0:
  print "Entering the display mode....."
  display = Display(visible=0, size=(800, 600))
  display.start()

print "Creating the web driver instance....."
driver = webdriver.Firefox()
driver.get('https://www.linkedin.com/login')
time.sleep(15)

print "Authenticating to LinkedIn....."
user = driver.find_element_by_id('username')
passwd = driver.find_element_by_id('password')
submit = driver.find_element(By.XPATH, '//button[text()="Sign in"]')

user.send_keys(username)
passwd.send_keys(password)
submit.click()
time.sleep(15)

print "Going to connections page....."
driver.get('https://www.linkedin.com/mynetwork')
time.sleep(20)

print "Starting the connection process....."
driver.execute_script("""
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function connections() {
  console.log('Lets begin...');
  para = document.createElement("P");
  para.innerText = "-1";
  para.id = '404040';
  document.body.appendChild(para);

  for (i = 0; i < 20; i++) {
    await sleep(2000);
    window.scrollTo(0, document.body.scrollHeight);
  }

  users = document.getElementsByClassName('full-width artdeco-button artdeco-button--2 artdeco-button--full artdeco-button--secondary ember-view');
  for (i = 0; i <= 1000000; i++) {
    await sleep(2000);
    console.log(i);
    document.getElementById('404040').innerText = i;
    if (users[i].innerText == "Connect"){ users[i].click(); }
  }

}

connections();
""")

time.sleep(45)

while(1):
  time.sleep(2)
  val = driver.execute_script("return document.getElementById('404040').innerText")
  if val != '-1': print ">>> Sending connection to user:", int(val)+1
  if driver.execute_script("return document.body.innerText.search('out of invitations')") != -1:
    print "You are out of invitations for now."
    time.sleep(2)
    driver.close()
    if visible == 0: display.stop()
    exit()

time.sleep(45)

print "The connection process completed successfully."
driver.close()
if visible == 0: display.stop()
