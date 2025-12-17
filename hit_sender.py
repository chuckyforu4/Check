import requests
import random

def send(cc, last, username, time_taken):
    ii = cc[:6]

    random_amount1 = random.randint(1, 4)
    random_amount2 = random.randint(1, 99)

    try:
        response = requests.get(f'https://bins.antipublic.cc/bins/{ii}')
        data = response.json()

        if response.status_code == 200:
            bank = data.get("bank", "Unknown")
            emj = data.get("country_flag", "🏳️")
            do = data.get("country", "Unknown")
            dicr = data.get("brand", "Unknown")
            typ = data.get("type", "Unknown")
        else:
            print(f"API Error: {data.get('error', 'Unknown error')}")
            bank = emj = do = dicr = typ = 'Unknown'
    except Exception as e:
        print(f"Error fetching data from API: {e}")
        bank = emj = do = dicr = typ = 'Unknown'

    msg1 = f"""
𝗚𝗔𝗧𝗘𝗪𝗔𝗬 ➜ Will Be Charge {random_amount1}.{random_amount2}$ 💳

𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘 ➜ {last}     
𝗖𝗖 ➜ <code>{cc}</code>       
𝗕𝗜𝗡 ➜ {ii}                   
𝗖𝗢𝗨𝗡𝗧𝗥𝗬 ➜ {do}               
𝗕𝗔𝗡𝗞 ➜ {bank}                
𝗙𝗟𝗔𝗚 ➜ {emj}                 

Check by @Chuckyforu4
𝗕𝗼𝘁 𝗯𝘆: @Chuckyforu4
"""
    return msg1
