import duckdb
import pandas as pd



def load_stop_dl_data() -> pd.DataFrame:
    df = duckdb.query(
        """
        SELECT route, dir, dl, stop
        FROM read_csv_auto('data/hfp_from_mqtt_2025-05-26.csv')
    """
    ).to_df()
    return df

def load_route_data() -> pd.DataFrame:
    df = duckdb.query(
        """
        SELECT DISTINCT route,
        FROM read_csv_auto('data/hfp_from_mqtt_2025-05-26.csv')
    """
    ).to_df()
    return df

def load_dir_data() -> pd.DataFrame:
    df = duckdb.query(
        """
        SELECT DISTINCT dir,
        FROM read_csv_auto('data/hfp_from_mqtt_2025-05-26.csv')
    """
    ).to_df()
    return df


def load_coordinate_data() -> pd.DataFrame:
    df = duckdb.query(
        """
        SELECT route, dir, lat, long, spd
        FROM read_csv_auto('data/hfp_from_mqtt_2025-05-26.csv')
    """
    ).to_df()
    return df
