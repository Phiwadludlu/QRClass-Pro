def filter(text, src):
        res = []
        for i in src:
            for k, v in i.items():
                if k in ["code","name","level"]:
                    match = v.lower().startswith(text)
                    if match:
                        res.append(i)
                        break
        return res