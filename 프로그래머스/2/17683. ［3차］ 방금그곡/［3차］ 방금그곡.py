def solution(m, musicinfos):
    answer_title = ""
    answer_time = 0
    
    m = replace_sharp(m)
    
    for musicinfo in musicinfos:
        start_time, end_time, title, sheet = musicinfo.split(",")
        play_time = get_minutes(end_time) - get_minutes(start_time)
        sheet = replace_sharp(sheet)
        notes = ""
        time = play_time
        
        while time >= len(sheet):
            notes += sheet
            time -= len(sheet)
        
        notes += sheet[:play_time % len(sheet)]
        
        if m in notes and answer_time < play_time:
            answer_title = title
            answer_time = play_time
        
    if answer_title == "":
        answer_title = "(None)"
    
    return answer_title


def get_minutes(time):
    hour, minute = time.split(":")
    return int(hour) * 60 + int(minute)


def replace_sharp(notes):
        notes = notes.replace("C#", "H");
        notes = notes.replace("D#", "I");
        notes = notes.replace("F#", "J");
        notes = notes.replace("G#", "K");
        notes = notes.replace("A#", "L");
        notes = notes.replace("B#", "M");
        return notes;
