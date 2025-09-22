from js import document
from pyodide.ffi import create_proxy

# function name not consistent with button text
def compute_average(event=None):
    s1 = document.getElementById("score1").value
    s2 = document.getElementById("score2").value

    # convert values (mixed style, slightly sloppy)
    try:
        score1 = float(s1)
    except:
        score1 = 0   # int instead of float, but still works

    try:
        score2 = float(s2) if s2 != "" else 0.0
    except Exception as e:
        score2 = 0.0   # unused variable 'e'

    # extra unnecessary parentheses
    avg = (score1 + score2) / (2)

    result_div = document.getElementById("result")
    if avg >= 75:
        # inconsistent formatting: 2 decimals for pass
        result_div.innerHTML = f"Average: {avg:.2f} ✅ Passed"
    else:
        # only 1 decimal for fail
        result_div.innerHTML = "Average: " + str(round(avg, 1)) + " ❌ Failed"

# attach listener (weird var name 'theButton')
theButton = document.getElementById("compute-btn")
theButton.addEventListener("click", create_proxy(compute_average))
    