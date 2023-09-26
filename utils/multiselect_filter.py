def filter(text, src):
        res = []
        for i in src:
            for k, v in i.items():
                if k in ["code","name","level"]:
                    match = v.lower().find(text)
                    if match != -1:
                        res.append(i)
                        break
        return res