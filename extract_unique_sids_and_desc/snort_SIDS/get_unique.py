

SET_NO = "9_recorded"



def main():
    file = open(f"set{SET_NO}/sids.txt", "r")
    sids = []
    for line in file:
        sids.append(int(line.replace("\n", "")))

    unique_sids = []
    for sid in sids:
        if sid not in unique_sids:
            unique_sids.append(sid)

    try: unique_sids.remove('')
    except: pass

    unique_sids = sorted(unique_sids)
    [print(s) for s in unique_sids]

    alerts_file = open(f"set{SET_NO}/snort_output.txt", "r")
    alerts = []
    [alerts.append(line.replace("\n", "")) for line in alerts_file]
    print(alerts[0:10])

    for sid in unique_sids:
        found = False
        count = 0
        while not found:
            curr_alert = alerts[count]
            # print(curr_alert)
            if ":"+str(sid)+":" in curr_alert:
                print(f"{sid} -> {curr_alert}")
                found = True
            count += 1


if __name__ == "__main__":
    main()
