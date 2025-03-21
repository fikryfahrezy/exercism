def translate(text, consonant_count = 0):
    if " " in text:
        new_text = ""
        for sub_text in text.split(" "):
            new_text += translate(sub_text) + " "
        return new_text.strip()
    if text[0] in "aiueo" or text[:2] == "xr" or text[:2] == "yt":
        return text + "ay"
    if text[:2] == "qu":
        return text[2:] + text[:2] + "ay"
    if text[0] == "y" and consonant_count != 0:
        return text + "ay"
    if text[0] in "bcdfghjklmnpqrstvwxyz":
        consonant_count += 1
        return translate(text[1:] + text[0], consonant_count)
    return text