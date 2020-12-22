from datetime import datetime


def writelog(text, level="INFO", fileout=True):

    content = "{datetime} => {level}: {text}\n".format(
        datetime=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        level=level,
        text=text
    )

    print(content, end="")

    if fileout:
        with open("../logs/log.log", "a") as log_file_obj:
            log_file_obj.write(content)
            log_file_obj.close()
