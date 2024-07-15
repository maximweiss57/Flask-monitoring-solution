from flask import Flask, render_template
import psutil

app = Flask(__name__)

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_ram_usage():
    memory_info = psutil.virtual_memory()
    return memory_info.percent

def get_free_memory():
    memory_info = psutil.virtual_memory()
    return memory_info.available / (1024 ** 2)


@app.route("/")
def hello_world():
    while True:
        cpu_usage = get_cpu_usage()
        ram_usage = get_ram_usage()
        free_memory = get_free_memory()
        return render_template('output.html', cpu_usage=cpu_usage, ram_usage=ram_usage, free_memory=free_memory)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
    