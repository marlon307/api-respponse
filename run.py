import uvicorn


if __name__ == "__main__":
    uvicorn.run("main:app", env_file=".env", reload=True)
