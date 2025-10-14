import argparse, datetime as dt, os, sys, requests
BASE_URL = 'https://data.cityofnewyork.us/resource/erm2-nwe9.csv'
def build_params(start=None, end=None, limit=50000):
    params = {'$limit': limit}
    if start and end:
        params['$where'] = f"created_date between '{start}T00:00:00' and '{end}T23:59:59'"
    elif start:
        params['$where'] = f"created_date >= '{start}T00:00:00'"
    elif end:
        params['$where'] = f"created_date <= '{end}T23:59:59'"
    params['$select'] = ','.join([
        'unique_key','created_date','closed_date','agency','agency_name',
        'complaint_type','descriptor','location_type','incident_zip','incident_address',
        'borough','latitude','longitude'
    ])
    return params
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--days', type=int, default=60)
    ap.add_argument('--start', type=str)
    ap.add_argument('--end', type=str)
    ap.add_argument('--limit', type=int, default=100000)
    args = ap.parse_args()
    os.makedirs('data/raw', exist_ok=True)
    if args.start or args.end:
        start = args.start or (dt.date.today() - dt.timedelta(days=args.days)).isoformat()
        end = args.end or dt.date.today().isoformat()
        out = f'data/raw/nyc311_{start}_{end}.csv'
        params = build_params(start, end, args.limit)
    else:
        end_date = dt.date.today()
        start_date = end_date - dt.timedelta(days=args.days)
        start = start_date.isoformat()
        end = end_date.isoformat()
        out = 'data/raw/nyc311_last60d.csv'
        params = build_params(start, end, args.limit)
    print(f'Fetching NYC311 rows from {start} to {end} ...')
    try:
        r = requests.get(BASE_URL, params=params, timeout=90)
    except Exception as e:
        print('Download error:', e); sys.exit(1)
    if r.status_code != 200:
        print('Download failed:', r.status_code, r.text[:500]); sys.exit(1)
    with open(out, 'wb') as f:
        f.write(r.content)
    print(f'✅ Saved: {out} ({len(r.content)/1024/1024:.2f} MB)')
if __name__ == '__main__':
    main()
