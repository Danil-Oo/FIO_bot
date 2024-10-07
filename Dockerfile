FROM python:3.10-slim
ENV TOKEN='7026488469:AAFICmuouLznJiqHiOU9xGU3ExQlA8BG-pc'
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "bot.py"]