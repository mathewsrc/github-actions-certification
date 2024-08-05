import polars as pl


def main():
    df = pl.DataFrame(
        {
            "a": [1, 2, 3],
            "b": [4, 5, 6],
        }
    )
    print()
    print(f'::set-output name=shape::{df.shape}')
    
if __name__ == "__main__":
    main()