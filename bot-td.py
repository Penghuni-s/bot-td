require 'requests/sugar'
require 'thread/pool'
require 'io/console'
require 'net/http'
require 'digest'
require 'json'
require 'erb'
require 'uri'
require 'os'

$logo = " \n\033[1;97m█████████
$MaxProcess = 30
$limits = 5000

def load()
  for x in [".   ", "..  ", "... ",".... ","\n"]
    $stdout.write("\r\033[92m[!] Please Wait"+x)
    $stdout.flush()
    sleep(1)
  end
end

def tik(teks)
  for x in teks.chars << "\n"
    $stdout.write(x)
    $stdout.flush()
    sleep(0.05)
  end
end

def convert_bytes(num)
  for i in ['B','KB','MB','GB','TB']
    if num < 1024.0
      return "%3.1f %s" % [num, i]
    else
      num /= 1024.0
    end
  end
end

def get(url)
  x = URI(url)
  y = Net::HTTP.get(x)
  return y
end

def login()
  begin
    system('clear')
    puts($logo)
    puts ("║-> \033[0;97m[\033[0;96m2\033[0;97m]\x1b[1;37;40m1. cookies")
    print ("╚═\x1b[1;91m▶\x1b[1;97m ")
    if ask =="":
			login()
		elif ask == "1" or ask == "01":
			cookie()
		else:
			login()

def cookie():
	logo()
	print("\n \033[0;97m[\033[0;93m*\033[0;97m] hello")
	cookie = raw_input(" \033[0;97m[\033[0;92m+\033[0;97m] Masukan Cookies bro : \033[0;96m")
	try:
		data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
		'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', # Jangan Di Ganti Ea Anjink.
		'referer'                   : 'https://m.facebook.com/',
		'host'                      : 'm.facebook.com',
		'origin'                    : 'https://m.facebook.com',
		'upgrade-insecure-requests' : '1',
		'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cache-control'             : 'max-age=0',
		'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'content-type'              : 'text/html; charset=utf-8'
		}, cookies = {
		'cookie'                    : cookie
		})
		find_token = re.search('(EAAA\w+)', data.text)
		hasil    = " \033[0;97m[\033[0;91m!\033[0;97m] Your Cookie Invalid" if (find_token is None) else '\n* Your fb access token : ' + find_token.group(1)
	except requests.exceptions.ConnectionError:
		print(' \033[0;97m[\033[0;91m!\033[0;97m] No Connection')
	cookie = open("login.txt", 'w')
	cookie.write(find_token.group(1))
	cookie.close()
	
	def menu()
  system('clear')
  puts ($logo)
  puts ("\033[97m╔══════════════════════════════════════════════════╗")
  puts ("\033[97m║\033[91m[\033[96m✓\033[91m] \033[97mName : \033[92m" + $name + " "*(39 - $name.length()) + "\033[97m║")
  puts ("\033[97m║\033[91m[\033[96m✓\033[91m] \033[97mID.  : \033[92m" + $id + " "*(39 - $id.length()) + "\033[97m║")
  puts ("\033[97m╠══════════════════════════════════════════════════╝")
  puts ("║-> \x1b[1;37;40m1. MyFrofil")
  puts ("║-> \x1b[1;37;40m2. User Information")
  puts ("║-> \x1b[1;37;40m3. Hack Facebook Account")
  puts ("║-> \x1b[1;37;40m4. Bot")
  puts ("║-> \x1b[1;37;40m5. Others")
  puts ("║-> \x1b[1;37;40m6. Feedback")
  puts ("║-> \x1b[1;37;40m7. Update")
  puts ("║-> \x1b[1;37;40m8. Logout")
  puts ("║-> \x1b[1;37;40m0. exit")
  puts ("\x1b[1;37;40m║")
  print ("╚═\x1b[1;91m▶\x1b[1;97m ")
  pilih = gets.chomp()
  if pilih == '1' or pilih == '01'
    MyFrofil()
    print ("\n\033[91m[\033[92mBack\033[91m] ")
    gets
    menu()
  elsif pilih == '2' or pilih == '02'
    Info()
    print ("\n\033[91m[\033[92mBack\033[91m] ")
    gets
    menu()
  elsif pilih == '3' or pilih == '03'
    Hamker()
  elsif pilih == '4' or pilih == '04'
    Bot()
  elsif pilih == '5' or pilih == '05'
    lain()
  elsif pilih == '6' or pilih == '06'
    system ("xdg-open https://wa.me/6285754629509/")
    sleep(0.9)
  elsif pilih == '7' or pilih == '07'
    update()
  elsif pilih == '8' or pilih == '08'
    print ("Do You Want To Continue? [Y/n] ")
    sure = gets.chomp()
    if sure.downcase == 'y'
      puts ("#{$0} : Deleting File login.txt")
      sleep(0.3)
      begin
        File.delete('login.txt')
        abort ("#{$0} : Successfully Deleting the login.txt file")
      rescue
        puts ("#{$0} : Failed to delete the login.txt file")
      end
    else
      menu()
    end
  elsif pilih == '0' or pilih == '00'
    abort ("\033[91m[!] Exit")
  else
    puts ("\033[93m[!] Invalid Input")
    sleep(0.9)
    menu()
  end
end

def Bot()
  system("clear")
  puts ($logo)
  puts ("Welcome To Bot Menu :)")
  puts ("\033[97m═"*52)
  puts ("\033[97m║-> \x1b[1;37;40m1. Post Reaction")
  puts ("\033[97m║-> \x1b[1;37;40m2. Post comments")
  puts ("\033[97m║-> \x1b[1;37;40m3. Add Friend")
  puts ("\033[97m║-> \x1b[1;37;40m4. Follow")
  puts ("\033[97m║-> \x1b[1;37;40m5. Share Post")
  puts ("\033[97m║-> \x1b[1;37;40m6. Delete Post")
  puts ("\033[97m║-> \x1b[1;37;40m7. Unfriends")
  puts ("\033[97m║-> \x1b[1;37;40m8. Unfollow")
  puts ("\033[97m║-> \x1b[1;32;40m0. Back")
  puts ("\x1b[1;37;40m║")
  print ("╚═\x1b[1;91m▶\x1b[1;97m ")
  bots = gets.chomp()
  if bots == '1' or bots == '01'
    ReactPostMenu()
  elsif bots == '2' or bots == '02'
    CommentPostMenu()
  elsif bots == '3' or bots == '03'
    AddFriendMenu()
  elsif bots == '4' or bots == '04'
    FollowMenu()
  elsif bots == '5' or bots == '05'
    system('clear')
    puts ($logo)
    puts ("\033[97m═"*52)
    print ("\033[97m[+] Post Id : ")
    id = gets.chomp() ; id = id.tr(" ","")
    req = get("https://graph.facebook.com/#{id}?fields=from,id&access_token=#{$token}")
    res = JSON.parse(req)
    if not res.key? ('id')
      puts ("\033[93m[+] Posts Not Found")
    else
      SharePostMenu(link = "https://www.facebook.com/#{res['id']}")
    end
    print ("\n\033[91m[\033[92mBack\033[91m] ")
    gets
    Bot()
  elsif bots == '6' or bots == '06'
    DeleteAllPost()
  elsif bots == '7' or bots == '07'
    Unfriend()
  elsif bots == '8' or bots == '08'
    unfollow()
  elsif bots == '0' or bots == '00'
    menu()
  else
    puts ("\033[93m[!] Invalid Input")
    sleep(0.9)
    Bot()
  end
end

def ReactPostMenu()
  system("clear")
  puts ($logo)
  puts ("\033[97m═"*52)
  puts ("\033[97m║-> \x1b[1;37;40m1. Target Post Reaction")
  puts ("\033[97m║-> \x1b[1;37;40m2. Group Post Reactions")
  puts ("\033[97m║-> \x1b[1;37;40m3. Random Target Post Reaction")
  puts ("\033[97m║-> \x1b[1;37;40m4. Random Group Post Reaction")
  puts ("\033[97m║-> \x1b[1;32;40m0. Back")
  puts ("\x1b[1;37;40m║")
  print ("╚═\x1b[1;91m▶\x1b[1;97m ")
  mana = gets.chomp()
  if mana == '1' or mana == '01'
    ReactPost()
  elsif mana == '2' or mana == '02'
    ReactGruop()
  elsif mana == '3' or mana == '03'
    ReactPostRandom()
  elsif mana == '4' or mana == '04'
    ReactGruopRandom()
  elsif mana == '0' or mana == '00'
    Bot()
  else
    puts ("\033[93m[!] Invalid Input")
    sleep(0.9)
    ReactPostMenu()
  end
end

def CommentPostMenu()
  system("clear")
  puts ($logo)
  puts ("\033[97m═"*52)
  puts ("\033[97m║-> \x1b[1;37;40m1. Comment Target Post")
  puts ("\033[97m║-> \x1b[1;37;40m2. Comment Group Post")
  puts ("\033[97m║-> \x1b[1;37;40m3. Spam Comment")
  puts ("\033[97m║-> \x1b[1;32;40m0. Back")
  puts ("\x1b[1;37;40m║")
  print ("╚═\x1b[1;91m▶\x1b[1;97m ")
  mana = gets.chomp()
  if mana == '1' or mana == '01'
    CommentPost()
  elsif mana == '2' or mana == '02'
    CommentGroup()
  elsif mana == '3' or mana == '03'
    SpamComment()
  elsif mana == '0' or mana == '00'
    Bot()
  else
    puts ("\033[93m[!] Invalid Input")
    sleep(0.9)
    CommentPostMenu()
  end
end

def AddFriendMenu()
  system("clear")
  puts ($logo)
  puts ("\033[97m═"*52)
  puts ("\033[97m║-> \x1b[1;37;40m1. Add Friend From Target Id")
  puts ("\033[97m║-> \x1b[1;37;40m2. Add Friend From Friend")
  puts ("\033[97m║-> \x1b[1;37;40m3. Add Friend From File Id")
  puts ("\033[97m║-> \x1b[1;32;40m0. Back")
  puts ("\x1b[1;37;40m║")
  print ("╚═\x1b[1;91m▶\x1b[1;97m ")
  mana = gets.chomp()
  if mana == '1' or mana == '01'
    AddTarget()
  elsif mana == '2' or mana == '02'
   AddFriends()
  elsif mana == '3' or mana == '03'
   AddFile()
  elsif mana == '0' or mana == '00'
    Bot()
  else
    puts ("\033[93m[!] Invalid Input")
    sleep(0.9)
    AddFriendMenu()
  end
end

def FollowMenu()
  system("clear")
  puts ($logo)
  puts ("\033[97m═"*52)
  puts ("\033[97m║-> \x1b[1;37;40m1. Follow target Id")
  puts ("\033[97m║-> \x1b[1;37;40m2. Follow all friend")
  puts ("\033[97m║-> \x1b[1;37;40m3. Follow Friend from Friend")
  puts ("\033[97m║-> \x1b[1;37;40m4. Follow From File Id")
  puts ("\033[97m║-> \x1b[1;32;40m0. Back")
  puts ("\x1b[1;37;40m║")
  print ("╚═\x1b[1;91m▶\x1b[1;97m ")
  mana = gets.chomp()
  if mana == '1' or mana == '01'
    FolowTarget()
  elsif mana == '2' or mana == '02'
   FolowAll()
  elsif mana == '3' or mana == '03'
   FolowFromFriend()
  elsif mana == '4' or mana == '04'
    FolowFromFile()
  elsif mana == '0' or mana == '00'
    Bot()
  else
    puts ("\033[93m[!] Invalid Input")
    sleep(0.9)
    FollowMenu()
  end
end

def SharePostMenu(link)
  total = 0
  system('clear')
  puts ($logo)
  puts ("\033[97m═"*52)
  puts ("\033[97m║-> \x1b[1;37;40m1. Share To Facebook")
  puts ("\033[97m║-> \x1b[1;37;40m2. Share on a Friend's Timeline")
  puts ("\033[97m║-> \x1b[1;37;40m3. Share on a Page")
  puts ("\033[97m║-> \x1b[1;37;40m4. Share in WhatsApp")
  puts ("\033[97m║-> \x1b[1;32;40m0. Back")
  puts ("\x1b[1;37;40m║")
  print ("╚═\x1b[1;91m▶\x1b[1;97m ")
  mana = gets.chomp()
  if mana == '1' or mana == '01'
    system('clear')
    puts ($logo)
    puts ("\033[97m[!] Use <> For New Line")
    puts ("\033[97m═"*52)
    print ("\033[97m[+] Message : ")
    msg = gets.chomp()
    msg = msg.tr("<>","\n")
    req = get("https://graph.facebook.com/me/feed?method=POST&link=#{link}&message=#{msg}&access_token=#{$token}")
    res = JSON.parse(req)
    if res.key? ('id')
      puts ("\033[92m[✓] Success : #{res['id']}")
    else
      puts ("\033[93m[!] Failed  : nil")
    end
  elsif mana == '2' or mana == '02'
    system('clear')
    puts ($logo)
    puts ("\033[97m[!] Use <> For New Line")
    puts ("\033[97m═"*52)
    print ("\033[97m[+] Message : ")
    msg = gets.chomp()
    msg = msg.tr("<>","\n")
    print ("\033[97m[+] Limit (\033[92mMax \033[91m#{$limits}\033[97m) : ")
    limit = gets.to_i
    a = get("https://graph.facebook.com/me/friends?fields=id,name&limit=#{limit}&access_token=#{$token}")
    b = JSON.parse(a)
    if not b.key? ("data")
      abort ("\033[91m[!] Error")
    elsif b['data'].empty?
      puts ("\033[93m[+] Your Account Has No Friends")
    else
      puts ("\033[97m[+] CTRL + C TO STOP")
      puts ("\033[97m[+] Pleace Wait...")
      puts ("\033[97m═"*52)
      for i in b['data']
        begin
          nama = i['name']
          id = i['id']
          req = get("https://graph.facebook.com/#{id}/feed?method=POST&link=#{link}&message=#{msg}&access_token=#{$token}")
          res = JSON.parse(req)
          if res.key? ("id")
            total += 1
            puts ("\033[92m[✓] Success : #{nama} --> #{id}")
          else
            puts ("\033[93m[!] Failed  : #{nama} --> #{id}")
          end
          sleep(0.2)
        rescue SocketError
          puts ("\033[91m[!] No Connection")
          sleep(0.9)
        rescue Interrupt
          puts ("\n") ; break
        end
      end
      puts ("\033[97m═"*52)
      puts ("\033[92m[✓] Finish #{total}")
    end
  elsif mana == '3' or mana == '03'
    system('clear')
    puts($logo)
    puts ("\033[97m[!] Use <> For New Line")
    puts ("\033[97m═"*52)
    print ("\033[97m[+] Message : ")
    msg = gets.chomp()
    msg = msg.tr("<>","\n")
    print ("\033[97m[+] Limit : ")
    limit = gets.to_i
    a = get("https://graph.facebook.com/"+ $id + "/accounts?fields=name,access_token&limit=#{limit}&access_token="+$token)
    b = JSON.parse(a)
    if not b.key? ("data")
      abort ("\033[91m[!] Error")
    elsif b['data'].empty?
      puts ("\033[93m[+] Your Account Doesn't Have a Page")
    else
      puts ("\033[97m[+] CTRL + C TO STOP")
      puts ("\033[97m[+] Pleace Wait...")
      puts ("\033[97m═"*52)
      for i in b['data']
        begin
          nama = i['name']
          id = i['id']
          token = i['access_token']
          req = get("https://graph.facebook.com/#{id}/feed?method=POST&link=#{link}&message=#{msg}&access_token=#{token}")
          res = JSON.parse(req)
          if res.key? ("id")
            total += 1
            puts ("\033[92m[✓] Success : #{nama} --> #{id}")
          else
            puts ("\033[93m[!] Failed  : #{nama} --> #{id}")
          end
          sleep(0.2)
        rescue SocketError
          puts ("\033[91m[!] No Connection")
          sleep(0.9)
        rescue Interrupt
          puts ("\n") ; break
        end
      end
      puts ("\033[97m═"*52)
      puts ("\033[92m[✓] Finish #{total}")
    end
  elsif mana == '4' or mana == '04'
    system('clear')
    puts ($logo)
    puts ("\033[97m═"*52)
    sukses = system("xdg-open --chooser whatsapp://send?text=#{link}")
    if sukses
      puts ("\033[92m[✓] Successfully Opening the WhatsApp Application")
    else
      puts ("\033[93m[+] Failed to Open the WhatsApp Application")
    end
  else
    puts ("\033[93m[+] Invalid Input")
  end
end

def React()
  loop do
    system("clear")
    puts ($logo)
    puts ("\033[97m═"*52)
    puts ("\033[97m║-> \x1b[1;34;40m1. LIKE")
    puts ("\033[97m║-> \x1b[1;35;40m2. LOVE")
    puts ("\033[97m║-> \x1b[1;33;40m3. HAHA")
    puts ("\033[97m║-> \x1b[1;33;40m4. WOW")
    puts ("\033[97m║-> \x1b[1;36;40m5. SAD")
    puts ("\033[97m║-> \x1b[1;31;40m6. ANGRY")
    puts ("\x1b[1;37;40m║")
    print ("╚═\x1b[1;91m▶\x1b[1;97m ")
    pilih = gets.chomp()
    if pilih == '1' or pilih == '01'
      return 'LIKE'
    elsif pilih == '2' or pilih == '02'
      return 'LOVE'
    elsif pilih == '3' or pilih == '03'
      return 'HAHA'
    elsif pilih == '4' or pilih == '04'
      return 'WOW'
    elsif pilih == '5' or pilih == '05'
      return 'SAD'
    elsif pilih == '6' or pilih == '06'
      return 'ANGRY'
    else
      puts ("\033[93m[!] Invalid Input")
      sleep(1)
    end
  end
end


def ReactPost()
  begin
    total = 0
    tipe = React()
    system('clear')
    puts ($logo)
    puts ("\033[97m═"*52)
    print ("\033[97m[+] Target Id : ")
    id = gets.chomp() ; id = id.tr(" ","")
    print ("\033[97m[+] Limit : ")
    limit = gets.to_i
    puts ("\033[97m[+] Loading")
    puts ("\033[97m═"*52)
    x = get('https://graph.facebook.com/' + id + '?fields=feed.limit(' + limit.to_s + ')&access_token=' + $token)
    y = JSON.parse(x)
    for z in y['feed']['data']
      y = z['id']
      begin
        p = Requests.post('https://graph.facebook.com/' + y + '/reactions?type=' + tipe + '&access_token=' + $token)
        puts ("\033[97m[\033[92m✓\033[97m] \033[92mSuccess \033[97m-> \033[96m%s \033[97m-> \033[93m%s" % [tipe, y])
        total += 1
      rescue 
        puts ("\033[97m[\033[93m!\033[97m] \033[91mFailed \033[97m-> \033[96m%s \033[97m-> \033[93m%s" % [tipe, y])
      rescue Interrupt
        puts ("\n")
        break
      end
    end
    puts ("\033[97m═"*52)
    puts ("\033[92m[✓] Finish "+ total.to_s)
    print ("\n\033[91m[\033[92mBack\033[91m] ")
    gets
    ReactPostMenu()
  rescue NoMethodError
    if y.include? ('id')
      puts ("\033[93m[!] No posts :(")
      print ("\n\033[91m[\033[92mBack\033[91m] ")
      gets
      ReactPostMenu()
    else
      puts ("\033[93m[!] User Not Found")
      print ("\n\033[91m[\033[92mBack\033[91m] ")
      gets
      ReactPostMenu()
    end
  end
end

def ReactPostRandom()
  begin
    total = 0
    tipe = ['LIKE','LOVE','HAHA','WOW','SAD','ANGRY']
    system('clear')
    puts ($logo)
    puts ("\033[97m═"*52)
    print ("\033[97m[+] Target Id : ")
    id = gets.chomp() ; id = id.tr(" ","")
    print ("\033[97m[+] Limit : ")
    limit = gets.to_i
    puts ("\033[97m[+] Loading")
    puts ("\033[97m═"*52)
    x = get('https://graph.facebook.com/' + id + '?fields=feed.limit(' + limit.to_s + ')&access_token=' + $token)
    y = JSON.parse(x)
    for z in y['feed']['data']
      y = z['id']
      reaksi = tipe.sample
      begin
        p = Requests.post('https://graph.facebook.com/' + y + '/reactions?type=' + reaksi + '&access_token=' + $token)
        puts ("\033[97m[\033[92m✓\033[97m] \033[92mSuccess \033[97m-> \033[96m%s \033[97m-> \033[93m%s" % [reaksi, y])
        total += 1
      rescue 
        puts ("\033[97m[\033[93m!\033[97m] \033[91mFailed \033[97m-> \033[96m%s \033[97m-> \033[93m%s" %[reaksi, y])
      rescue Interrupt
        puts ("\n")
        break
      end
    end
    puts ("\033[97m═"*52)
    puts ("\033[92m[✓] Finish "+ total.to_s)
    print ("\n\033[91m[\033[92mBack\033[91m] ")
    gets
    ReactPostMenu()
  rescue NoMethodError
    if y.include? ('id')
      puts ("\033[93m[!] No posts :(")
      print ("\n\033[91m[\033[92mBack\033[91m] ")
      gets
      ReactPostMenu()
    else
      puts ("\033[93m[!] User Not Found")
      print ("\n\033[91m[\033[92mBack\033[91m] ")
      gets
      ReactPostMenu()
    end
  end
end

def CommentPost()
  begin
    total = 0
    system ('clear')
    puts ($logo)
    puts ("\033[97m[!] Use <> For New Line")
    puts ("\033[97m═"*52)
    print ("\033[97m[+] Target Id : ")
    id = gets.chomp() ; id = id.tr(" ","")
    print ("\033[97m[+] Comment : ")
    body = gets.chomp()
    print ("\033[97m[+] Limit : ")
    limit = gets.to_i
    puts ("\033[97m[+] Loading....")
    puts ("\033[97m═"*52)
    body = body.tr("<>","\n")
    teks = ERB::Util.url_encode(body)
    a = get('https://graph.facebook.com/' + id + '?fields=feed.limit(' + limit.to_s + ')&access_token=' + $token)
    b = JSON.parse(a)
    for c in b['feed']['data']
      id = c['id']
      begin
        Requests.post("https://graph.facebook.com/%s/comments?message=%s&access_token=%s" % [id, teks, $token])
        puts ("\033[97m[\033[92m✓\033[97m] \033[92mSuccess \033[97m-> \033[96m%s... \033[97m-> \033[93m%s" % [body[0..10], id]) if body.length > 10
        puts ("\033[97m[\033[92m✓\033[97m] \033[92mSuccess \033[97m-> \033[96m%s \033[97m-> \033[93m%s" % [body, id]) if body.length <= 10
        total += 1
      rescue
        puts ("\033[97m[\033[93m!\033[97m] \033[91mFailed \033[97m-> \033[96m%s... \033[97m-> \033[93m%s" % [body[0..10], id]) if body.length > 10
        puts ("\033[97m[\033[93m!\033[97m] \033[91mFailed \033[97m-> \033[96m%s \033[97m-> \033[93m%s" % [body, id]) if body.length <= 10
      rescue Interrupt
        puts ("\n")
        break
      end
    end
    puts ("\033[97m═"*52)
    puts ("\033[92m[✓] Finish "+ total.to_s)
    print ("\n\033[91m[\033[92mBack\033[91m] ")
    gets
    CommentPostMenu()
  rescue NoMethodError
    if b.include? ('id')
      puts ("\033[93m[!] No posts :(")
      print ("\n\033[91m[\033[92mBack\033[91m] ")
      gets
      CommentPostMenu()
    else
      puts ("\033[93m[!] User Not Found")
      print ("\n\033[91m[\033[92mBack\033[91m] ")
      gets
      CommentPostMenu()
    end
  end
end

def ReactGruop()
   begin
    total = 0
    tipe = React()
    system('clear')
    puts ($logo)
    puts ("\033[97m═"*52)
    print ("\033[97m[+] Group Id : ")
    group = gets.chomp()
    print ("\033[97m[+] Limit : ")
    limit = gets.to_i
    puts ("\033[97m[!] CTRL + C TO STOP")
    puts ("\033[97m═"*52)
    a = get("https://graph.facebook.com/v3.0/%s?fields=feed.limit(%s)&access_token=%s" % [group,limit,$token])
    b = JSON.parse(a)
    for x in b['feed']['data']
      id = x['id']
      begin
        y = Requests.post("https://graph.facebook.com/%s/reactions?type=%s&access_token=%s" % [id,tipe,$token])
        puts ("\033[97m[\033[92m✓\033[97m] \033[92mSuccess \033[97m-> \033[96m%s \033[97m-> \033[93m%s" % [tipe,id])
        total += 1
      rescue
        puts ("\033[97m[\033[93m!\033[97m] \033[91mFailed \033[97m-> \033[96m%s \033[97m-> \033[93m%s" %[tipe, id])
      rescue Interrupt
        puts ("\n")
        break
      end
    end
    puts ("\033[97m═"*52)
    puts ("\033[92m[✓] Finish "+ total.to_s)
    print ("\n\033[91m[\033[92mBack\033[91m] ")
    gets
    ReactPostMenu()
  rescue NoMethodError
    if a.include? ('id')
      puts ("\033[93m[!] No posts :(")
      print ("\n\033[91m[\033[92mBack\033[91m] ")
      gets
      ReactPostMenu()
    else
      puts ("\033[93m[!] group Not Found")
      print ("\n\033[91m[\033[92mBack\033[91m] ")
      gets
      ReactPostMenu()
    end
  end
end

def ReactGruopRandom()
  begin
    total = 0
    tipe = ['LIKE','LOVE','HAHA','WOW','SAD','ANGRY']
    system('clear')
    puts ($logo)
    puts ("\033[97m═"*52)
    print ("\033[97m[+] Group id : ")
    id = gets.chomp() ; id = id.tr(" ","")
    print ("\033[97m[+] Limit : ")
    limit = gets.to_i
    puts ("\033[97m[!] CTRL + C TO STOP")
    puts ("\033[97m═"*52)
    x = get("https://graph.facebook.com/v3.0/%s?fields=feed.limit(%s)&access_token=%s" % [id,limit,$token])
    y = JSON.parse(x)
    for z in y['feed']['data']
      y = z['id']
      reaksi = tipe.sample
      begin
        Requests.post('https://graph.facebook.com/' + y + '/reactions?type=' + reaksi + '&access_token=' + $token)
        puts ("\033[97m[\033[92m✓\033[97m] \033[92mSuccess \033[97m-> \033[96m%s \033[97m-> \033[93m%s" % [reaksi, y])
        total += 1
      rescue 
        puts ("\033[97m[\033[93m!\033[97m] \033[91mFailed \033[97m-> \033[96m%s \033[97m-> \033[93m%s" %[reaksi, y])
      rescue Interrupt
        puts ("\n")
        break
      end
    end
    puts ("\033[97m═"*52)
    puts ("\033[92m[✓] Finish "+ total.to_s)
    print ("\n\033[91m[\033[92mBack\033[91m] ")
    gets
    ReactPostMenu()
  rescue NoMethodError
    if y.include? ('id')
      puts ("\033[93m[!] No posts :(")
      print ("\n\033[91m[\033[92mBack\033[91m] ")
      gets
      ReactPostMenu()
    else
      puts ("\033[93m[!] Group Not Found")
      print ("\n\033[91m[\033[92mBack\033[91m] ")
      gets
      ReactPostMenu()
    end
  end
end

def CommentGroup()
  begin
    total = 0
    system ('clear')
    puts ($logo)
    puts ("\033[97m[!] Use <> For New Line")
    puts ("\033[97m═"*52)
    print ("\033[97m[+] Group Id : ")
    id = gets.chomp() ; id = id.tr(" ","")
    print ("\033[97m[+] Comment : ")
    body = gets.chomp()
    print ("\033[97m[+] Limit : ")
    limit = gets.to_i
    body = body.tr("<>","\n")
    teks = ERB::Util.url_encode(body)
    a = get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + $token)
    b = JSON.parse(a)
    puts ("\033[97m[✓] Group : "+b['name'])
    puts ("\033[97m[!] CTRL + C TO STOP")
    puts ("\033[97m═"*52)
    c = get('https://graph.facebook.com/v3.0/' + id + '?fields=feed.limit(' + limit.to_s + ')&access_token=' + $token)
    d = JSON.parse(c)
    for e in d['feed']['data']
      begin
        Requests.post('https://graph.facebook.com/' + e['id'] + '/comments?message=' + teks + '&access_token=' + $token)
        puts ("\033[97m[\033[92m✓\033[97m] \033[92mSuccess \033[97m-> \033[96m%s... \033[97m-> \033[93m%s" % [body[0..10], e['id']]) if body.length > 10
        puts ("\033[97m[\033[92m✓\033[97m] \033[92mSuccess \033[97m-> \033[96m%s \033[97m-> \033[93m%s" % [body, e['id']]) if body.length <= 10
        total += 1
      rescue
        puts ("\033[97m[\033[93m!\033[97m] \033[91mFailed \033[97m-> \033[96m%s... \033[97m-> \033[93m%s" % [body[0..10], e['id']]) if body.length > 10
        puts ("\033[97m[\033[93m!\033[97m] \033[91mFailed \033[97m-> \033[96m%s \033[97m-> \033[93m%s" % [body, id]) if body.length <= 10
      rescue Interrupt
        puts ("\n")
        break
      end
    end
    puts ("\033[97m═"*52)
    puts ("\033[92m[✓] Finish "+ total.to_s)
    print ("\n\033[91m[\033[92mBack\033[91m] ")
    gets
    CommentPostMenu()
  rescue NoMethodError, TypeError
    if b.include? ('id')
      puts ("\033[93m[!] No posts :(")
      print ("\n\033[91m[\033[92mBack\033[91m] ")
      gets
      CommentPostMenu()
    else
      puts ("\033[93m[!] Group Not Found")
      print ("\n\033[91m[\033[92mBack\033[91m] ")
      gets
      CommentPostMenu()
    end
  end
end

def AddTarget()
  system('clear')
  puts ($logo)
  puts ("\033[97m═"*52)
  print ("\033[97m[+] Target Id : ")
  id = gets.chomp() ; id = id.tr(" ","")
  a = get('https://graph.facebook.com/' + id + '?access_token=' + $token)
  b = JSON.parse(a)
  if b.include? ('name')
    puts ("\033[92m[+] Target : "+b['name'])
    puts ("\033[97m[+] Loading...")
    puts ("\033[97m═"*52)
    begin
      Requests.post('https://graph.facebook.com/me/friends/' + b['id'] + '?access_token=' + $token)
      puts ("\033[92m[✓] Name : "+b['name'])
      puts ("\033[92m[✓] Status : Success")
      print ("\n\033[91m[\033[92mBack\033[91m] ")
      gets
      AddFriendMenu()
    rescue
      puts ("\033[92m[✓] Name :"+b['name'])
      puts ("\033[92m[✓] Status : Failed")
      print ("\n\033[91m[\033[92mBack\033[91m] ")
      gets
      AddFriendMenu()
    end
  elsif b.include? ('error') and b['error']['code'] == 190
    abort ("\033[93m[!] "+b['error']['message'])
  else
    puts("\033[93m[!] Users Not Found")
    print ("\n\033[91m[\033[92mBack\033[91m] ")
    gets
    AddFriendMenu()
  end
end

def AddFriends()
  begin
    total = 0
    system("clear")
    puts ($logo)
    puts ("\033[97m═"*52)
    print ("\033[97m[+] Friend Id : ")
    id = gets.chomp() ; id = id.tr(" ","")
    print ("\033[97m[+] Limit : ")
    limit = gets.to_i
    a = get('https://graph.facebook.com/' + id + '?access_token=' + $token)
    b = JSON.parse(a)
    if b.include? ("name")
      tik("\033[97m[+] From "+b['name'])
      puts ("\033[97m[!] CTRL + C TO STOP")
      puts ("\033[97m═"*52)
      a = get('https://graph.facebook.com/%s?fields=friends.limit(%d)&access_token=%s' % [id,limit,$token])
      b = JSON.parse(a)
      for c in b['friends']['data']
        id = c['id']
        begin
          Requests.post('https://graph.facebook.com/me/friends/' + id + '?access_token=' + $token)
          puts ("\033[97m[\033[92m✓\033[97m] \033[92mSuccess : \033[96m%s --> \033[93m%s" % [c['name'],id])
          total += 1
        rescue
         puts ("\033[97m[\033[91m!\033[97m] \033[91mFailed  : \033[96m%s --> \033[93m%s" % [c['name'],id])
        rescue Interrupt
          puts ("\n")
          break
        end
      end
      puts ("\033[97m═"*52)
      puts ("\033[92m[✓] Finish "+ total.to_s)
      print ("\n\033[91m[\033[92mBack\033[91m] ")
      gets
      AddFriendMenu()
    else
      puts ("\033[93m[!] User Not Found")
      print ("\n\033[91m[\033[92mBack\033[91m] ")
      gets
      AddFriendMenu()
    end
  rescue NoMethodError
    puts ("\033[93m[+] There are no friends on the account")
    print ("\n\033[91m[\033[92mBack\033[91m] ")
    gets
    AddFriendMenu()
  end
end


def AddFile()
  total = 0
  system('clear')
  puts ($logo)
  puts ("\033[97m═"*52)
  print ("\033[97m[+] File Id : ")
  file = gets.chomp()
  print ("\033[97m[+] Limit : ")
  limit = gets.to_i
  if File.file? (file)
    files = File.readlines(file, chomp: true)
    puts ("\033[97m[!] CTRL + C TO STOP")
    puts ("\033[97m═"*52)
    for id in files[0...limit]
      begin
        a = get('https://graph.facebook.com/' + id + '?access_token=' + $token)
        b = JSON.parse(a)
        c = Requests.post('https://graph.facebook.com/me/friends/' + b['id'] + '?access_token=' + $token)
        puts ("\033[97m[\033[92m✓\033[97m] \033[92mSuccess : \033[96m%s --> \033[93m%s" % [b['name'], b['id']])
        total += 1
      rescue TypeError
        puts ("\033[97m[\033[91m!\033[97m] \033[91mNot Found -> "+id)
      rescue
        puts ("\033[97m[\033[91m!\033[97m] \033[91mFailed  : \033[96m%s --> \033[93m%s" % [b['name'], b['id']])
      rescue Interrupt
        puts ("\n")
        break
      end
    end
    puts ("\033[97m═"*52)
    puts ("\033[92m[✓] Finish "+ total.to_s)
    print ("\n\033[91m[\033[92mBack\033[91m] ")
    gets
    AddFriendMenu()
  else
    puts ("\033[93m[+] File Not Found")
    print ("\n\033[91m[\033[92mBack\033[91m] ")
    gets
    AddFriendMenu()
  end
end

def SpamComment()
  total = 0
  system("clear")
  puts ($logo)
  puts ("\033[97m[!] Use <> For New Line")
  puts ("\033[97m═"*52)
  print ("\033[97m[+] Post Id : ")
  id = gets.chomp() ; id = id.tr(" ","")
  a = get("https://graph.facebook.com/#{id}?access_token=#{$token}")
  b = JSON.parse(a)
  if not b.key? ('from')
    puts ("\033[93m[!] Post Not Found")
  else
    puts ("\033[97m[+] Posted By #{b['from']['name']}")
    print ("\033[97m[+] Comment : ")
    body = gets.chomp()
    msg = body.tr("<>","\n")
    print ("\033[97m[+] Limit   : ")
    limit = gets.to_i
    data = {"message"=>msg,"access_token"=>$token}
    url = URI("https://graph.facebook.com/#{id}/comments")
    puts ("\033[97m═"*52)
    limit.times do |i|
      req = Net::HTTP.post_form(url,data)
      res = JSON.parse(req.body)
      if res.key? ('id')
        total += 1
        puts ("\033[92m[✓] Success : #{body} -> #{id}") if body.length <= 10
        puts ("\033[92m[✓] Success : #{body[0...8]...} -> #{id}") if body.length > 10
      else
        puts ("\033[93m[!] Failed  : #{body} -> #{id}") if body.length <= 10
        puts ("\033[93m[!] Failed  : #{body[0...8]} -> #{id}") if body.length > 10
      end
    end
    puts ("\033[97m═"*52)
    puts ("\033[92m[✓] Finish "+ total.to_s)
    print ("\n\033[91m[\033[92mBack\033[91m] ")
    gets
    CommentPostMenu()
  end
end

def FolowTarget()
  system('clear')
  puts ($logo)
  puts ("\033[97m═"*52)
  print ("\033[97m[+] Target Id : ")
  id = gets.chomp() ; id = id.tr(" ","")
  a = get('https://graph.facebook.com/' + id + '?access_token=' + $token)
  b = JSON.parse(a)
  if b.include? ('name')
    puts ("\033[97m[+] Target : "+b['name'])
    puts ("\033[97m[+] Loading...")
    puts ("\033[97m═"*52)
    begin
      x =Requests.post('https://graph.facebook.com/' + b['id'] + '/subscribers?access_token=' + $token)
      puts ("\033[92m[✓] Name   : "+b['name'])
      puts ("\033[92m[✓] Status : Success")
      print ("\n\033[91m[\033[92mBack\033[91m] ")
      gets
      FollowMenu()
    rescue
      puts ("\033[92m[✓] Name   : "+b['name'])
      puts ("\033[92m[✓] Status : Failed")
      print ("\n\033[91m[\033[92mBack\033[91m] ")
      gets
      FollowMenu()
    end
  elsif b.include? ('error') and b['error']['code'] == 190
    abort ("\033[93[!] "+b['error']['message'])
  else
    puts("\033[93m[!] Users Not Found")
    print ("\n\033[91m[\033[92mBack\033[91m] ")
    gets
    FollowMenu()
  end
end

def FolowAll()
  total = 0
  system('clear')
  puts ($logo)
  puts ("\033[97m═"*52)
  puts ("\033[97m[+] Pleace Wait")
  x = get("https://graph.facebook.com/me/friends?access_token="+$token)
  y = JSON.parse(x)
  abort ("\033[93m[!] InValid Access Token") if y.include? ('error')
  puts ("\033[97m[!] CTRL + C TO STOP")
  puts ("\033[97m═"*52)
  for x in y['data']
    name = x['name']
    id = x['id']
    begin
      Requests.post('https://graph.facebook.com/' + id + '/subscribers?access_token=' + $token)
      puts ("\033[97m[\033[92m✓\033[97m] \033[92mSuccess : \033[96m%s --> \033[93m%s" % [name,id])
      total += 1
    rescue
      puts ("\033[97m[\033[91m!\033[97m] \033[91mFailed  : \033[96m%s --> \033[93m%s" % [name,id])
    rescue Interrupt
      puts("\n")
      break
    end
  end
  puts ("\033[97m═"*52)
  puts ("\033[92m[✓] Finish "+ total.to_s)
  print ("\n\033[91m[\033[92mBack\033[91m] ")
  gets
  FollowMenu()
end

def FolowFromFriend()
  begin
    total = 0
    system('clear')
    puts ($logo)
    puts ("\033[97m═"*52)
    print ("\033[97m[+] Friend Id : ")
    id = gets.chomp() ; id = id.tr(" ","")
    print ("\033[97m[+] Limit : ")
    limit = gets.to_i
    a = get('https://graph.facebook.com/' + id + '?access_token=' + $token)
    b = JSON.parse(a)
    if b.include? ("name")
      tik("\033[97m[+] From "+b['name'])
      puts ("\033[97m[!] CTRL + C TO STOP")
      puts ("\033[97m═"*52)
      a = get('https://graph.facebook.com/%s?fields=friends.limit(%d)&access_token=%s' % [id,limit,$token])
      b = JSON.parse(a)
      for c in b['friends']['data']
        id = c['id']
        begin
          Requests.post('https://graph.facebook.com/me/friends/' + id + '?access_token=' + $token)
          puts ("\033[97m[\033[92m✓\033[97m] \033[92mSuccess : \033[96m%s --> \033[93m%s" % [c['name'],id])
          total += 1
        rescue
          puts ("\033[97m[\033[91m!\033[97m] \033[91mFailed  : \033[96m%s --> \033[93m%s" % [c['name'],id])
        rescue Interrupt
          puts ("\n")
          break
        end
      end
      puts ("\033[97m═"*52)
      puts ("\033[92m[✓] Finish "+ total.to_s)
      print ("\n\033[91m[\033[92mBack\033[91m] ")
      gets
      FollowMenu()
    else
      puts ("\033[93m[!] User Not Found")
      print ("\n\033[91m[\033[92mBack\033[91m] ")
      gets
      FollowMenu()
    end
  rescue NoMethodError
    puts ("\033[93m[+] There are no friends on the account")
    print ("\n\033[91m[\033[92mBack\033[91m] ")
    gets
    FollowMenu()
  end
end

def FolowFromFile()
  total = 0
  system('clear')
  puts ($logo)
  puts ("\033[97m═"*52)
  print ("\033[97m[+] File Id : ")
  file = gets.chomp()
  print ("\033[97m[+] Limit : ")
  limit = gets.to_i
  if File.file? (file)
    files = File.readlines(file, chomp: true)
    puts ("\033[97m[!] CTRL + C TO STOP")
    puts ("\033[97m═"*52)
    for id in files[0...limit]
      begin
        a = get('https://graph.facebook.com/' + id + '?access_token=' + $token)
        b = JSON.parse(a)
        Requests.post('https://graph.facebook.com/' + id + '/subscribers?access_token=' + $token)
        puts ("\033[97m[\033[92m✓\033[97m] \033[92mSuccess : \033[96m%s --> \033[93m%s" % [b['name'], b['id']])
        total += 1
      rescue TypeError
        puts ("\033[97m[\033[91m!\033[97m] \033[91mNot Found -> "+id)
      rescue
        puts ("\033[97m[\033[91m!\033[97m] \033[91mFailed  : \033[96m%s --> \033[93m%s" % [b['name'], b['id']])
      rescue Interrupt
        puts ("\n")
        break
      end
    end
    puts ("\033[97m═"*52)
    puts ("\033[92m[✓] Finish "+ total.to_s)
    print ("\n\033[91m[\033[92mBack\033[91m] ")
    gets
    FollowMenu()
  else
    puts ("\033[93m[+] File Not Found")
    print ("\n\033[91m[\033[92mBack\033[91m] ")
    gets
    FollowMenu()
  end
end

def DeleteAllPost()
  total = 0
  system('clear')
  puts($logo)
  puts ("\033[97m═"*52)
  puts ("\033[97m[+] From "+$name)
  puts ("\033[97m[+] CTRL + C TO STOP")
  puts ("\033[97m[+] START..")
  puts ("\033[97m═"*52)
  a = get('https://graph.facebook.com/me/feed?access_token=' + $token)
  b = JSON.parse(a)
  for post in b['data']
    id = post['id']
    begin
     c = get('https://graph.facebook.com/' + id + '?method=delete&access_token=' + $token)
     d = JSON.parse(c)
     puts ("\033[97m[\033[92m✓\033[97m] \033[92mSuccess : "+id)
     total += 1
    rescue
     puts ("\033[97m[\033[91m!\033[97m] \033[91mFailed : "+id)
    rescue Interrupt
      puts ("\n")
      break
    end
  end
  puts ("\033[97m═"*52)
  puts ("\033[92m[✓] Finish "+ total.to_s)
  print ("\n\033[91m[\033[92mBack\033[91m] ")
  gets
  Bot()
end

def Unfriend()
  begin
    hitung = 0
    system('clear')
    puts ($logo)
    puts ("\033[97m═"*52)
    puts ("\033[97m[+] From "+$name)
    x = get ("https://graph.facebook.com/me/friends?access_token="+$token)
    y = JSON.parse(x)
    total = y['data'].each{|i| i['id']}
    puts ("\033[97m[+] Total Friend : "+total.length.to_s)
    puts ("\033[97m[+] CTRL + C TO STOP")
    puts ("\033[97m[+] START")
    puts ("\033[97m═"*52)
    for x in y['data']
      name = x['name']
      id = x['id'].to_s
      begin
        Requests.delete('https://graph.facebook.com/me/friends?uid=' + id + '&access_token=' + $token)
        hitung += 1
        puts ("\033[97m[\033[92m✓\033[97m] \033[92mSuccess \033[97m: \033[93m"+name+" \033[97m--> \033[96m"+id)
      rescue
        puts ("\033[97m[\033[91m!\033[97m] \033[91mFailed \033[97m: \033[93m"+name+" \033[97m--> \033[96m"+id)
      end
    end
    puts ("\033[97m═"*52)
    puts ("\033[92m[✓] Finish "+ hitung.to_s)
    print ("\n\033[91m[\033[92mBack\033[91m] ")
    gets
    Bot()
  rescue NoMethodError
    puts ("\033[93m[+] Your Account Has No Friends")
    print ("\n\033[91m[\033[92mBack\033[91m] ")
    gets
    Bot()
  end
end

def unfollow()
  begin
    jadi = 0
    system('clear')
    puts ($logo)
    puts ("\033[97m═"*52)
    puts ("\033[97m[+] From "+$name)
    a = get("https://graph.facebook.com/me/subscribedto?limit=#{$limits}&access_token=#{$token}")
    b = JSON.parse(a)
    total = b['data'].each{|i| i['id']}
    puts ("\033[97m[+] Total Id "+total.length.to_s)
    puts ("\033[97m[+] CTRL + C TO STOP")
    puts ("\033[97m[+] START")
    puts ("\033[97m═"*52)
    for x in b['data']
      name = x['name']
      id = x['id']
      begin
        Requests.post('https://graph.facebook.com/' + id + '/subscribers?method=delete&access_token=' + $token)
        puts ("\033[97m[\033[92m✓\033[97m] \033[92mSuccess : \033[96m%s --> \033[93m%s" % [name,id])
        jadi += 1
      rescue
        puts ("\033[97m[\033[91m!\033[97m] \033[91mFailed  : \033[96m%s --> \033[93m%s" % [name,id])
      rescue Interrupt
        puts ("\n")
        break
      end
    end
    puts ("\033[97m═"*52)
    puts ("\033[92m[✓] Finish "+ jadi.to_s)
    print ("\n\033[91m[\033[92mBack\033[91m] ")
    gets
    Bot()
  rescue
    puts ("\033[93m[!] There is an error")
    print ("\n\033[91m[\033[92mBack\033[91m] ")
    gets
    Bot()
  end
end
