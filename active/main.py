
import os
import uvicorn

if __name__ == "__main__":
    try:
        uvicorn.run("fa:app", host="0.0.0.0", port=int(os.environ['PORT']), reload=False, log_level="debug", debug=True, workers=1, limit_concurrency=1, limit_max_requests=1)
    except Exception as e:
        print("Error on running uvicorn: "+str(e))