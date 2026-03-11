import subprocess

def extract_metrics(local_port="8000", api_key="key123456", file_name = "metrics"):
    cmd = f"""curl -s http://localhost:{local_port}/metrics -H "Authorization: Bearer {api_key}" | grep 'kv_cache_usage_perc' | awk '{{ metric=$1; value=$NF; gsub(/{{.*}}/, "", metric); printf("{{\\"metric\\":\\"%s\\",\\"value\\":%.5f}}\\n", metric, value) }}'"""
    subprocess.run(cmd, shell=True, check=True)
    cmd2 = f"""curl -s http://localhost:{local_port}/metrics -H "Authorization: Bearer {api_key}" | grep 'num_requests_running' | awk '{{ metric=$1; value=$NF; gsub(/{{.*}}/, "", metric); printf("{{\\"metric\\":\\"%s\\",\\"value\\":%.5f}}\\n", metric, value) }}'"""
    subprocess.run(cmd2, shell=True, check=True)
    cmd3 = f"""curl -s http://localhost:{local_port}/metrics -H "Authorization: Bearer {api_key}" | grep 'num_requests_waiting' | awk '{{ metric=$1; value=$NF; gsub(/{{.*}}/, "", metric); printf("{{\\"metric\\":\\"%s\\",\\"value\\":%.5f}}\\n", metric, value) }}'"""
    subprocess.run(cmd3, shell=True, check=True)

if __name__ == "__main__":
    extract_metrics()

extract_metrics()
