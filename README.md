# Data Engineering Exercise Solution

## Description

This repository contains the solution to the **Data Engineering** exercise from [Daniel Beach's Data Engineering Practice repository](https://github.com/danielbeach/data-engineering-practice/tree/main?tab=readme-ov-file), where the objective was to **download ZIP files** from a list of provided URLs, **extract the CSV files** from those ZIPs, and **store them in a local folder** named `downloads`.

## What Was Requested

The exercise required the following tasks:

1. **Download 10 files** from specified URLs.
2. **Extract the CSV files** from inside the ZIP files.
3. **Store the extracted files** in a folder named `downloads`.
4. If the URL was invalid or the file did not exist, the code should **ignore that URL** and continue with the remaining URLs.
5. **Use Docker** to run the code within a container, as specified in the instructions.

### Additional Tasks (Extra Credit):
- The exercise also requested implementing **asynchronous downloading** and using **ThreadPoolExecutor** for parallel downloads. This part has been implemented to improve the performance of downloading the files simultaneously.

## What Was Done

To resolve this exercise, the following steps were completed:

1. **Created the `create_downloads_dir` function**:
   - A function was created to ensure the `downloads` folder is created if it doesn’t already exist, using `os.makedirs()`.

2. **Developed the `download_file` function**:
   - The `download_file` function was implemented to download files from the provided URLs.
   - To check if the URL was valid (and avoid 404 errors), the function also performs a check using `requests.head()` before proceeding with the download.

3. **Implemented the `extract_csv` function**:
   - A function to extract the CSV file from each ZIP file was created using the `zipfile` library. After extracting, the ZIP file is deleted to save space.

4. **Asynchronous Downloads**:
   - The downloading of files was made **asynchronous** using `aiohttp` and `asyncio` to allow downloading multiple files simultaneously, improving performance.
   - The `download_files_concurrently` function was added to handle the concurrent download of files.

5. **Docker Integration**:
   - Docker was used to create a consistent environment for running the script, as required by the exercise.

   -