import data_handling
import data_analysis
import visualization

def main():
    # Load data
    file_path = "zara.csv"
    df = data_handling.load_data(file_path)

    # Analyze data
    grouped_data, sorted_df = data_analysis.analyze_data(df)

    # Perform visualizations
    visualization.plot_top_products_by_category(sorted_df)
    visualization.plot_total_sales_by_category(df)
    visualization.plot_sales_by_gender(df)
    visualization.plot_top_products_by_gender_section(sorted_df)

if __name__ == "__main__":
    main()
