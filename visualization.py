import matplotlib.pyplot as plt

def plot_top_products_by_category(df):
    """
    Plots top products by category.

    Parameters:
    - df (pd.DataFrame): Input DataFrame.
    """
    sorted_df = df.sort_values(by=['terms', 'Sales Volume'], ascending=[True, False])
    top_3_by_terms = sorted_df.groupby('terms').head(3)

    plt.figure(figsize=(10, 6))
    for term, data in top_3_by_terms.groupby('terms'):
        plt.bar(data['name'], data['Sales Volume'], label=term)

    plt.xlabel('Product Name')
    plt.ylabel('Sales Volume')
    plt.title('Top 3 Products by Sales Volume in Each Category')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Product Category', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

def plot_total_sales_by_category(df):
    """
    Plots total sales volume by product category.

    Parameters:
    - df (pd.DataFrame): Input DataFrame.
    """
    total_sales_by_terms = df.groupby('terms')['Sales Volume'].sum()

    plt.figure(figsize=(6, 4))
    total_sales_by_terms.plot(kind='bar', color='skyblue')
    plt.title('Total Sales Volume by Product Category')
    plt.xlabel('Product Category')
    plt.ylabel('Total Sales Volume')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def plot_sales_by_gender(df):
    """
    Plots total sales volume by gender.

    Parameters:
    - df (pd.DataFrame): Input DataFrame.
    """
    total_sales_by_gender = df.groupby('section')['Sales Volume'].sum()

    plt.figure(figsize=(6, 4))
    total_sales_by_gender.plot(kind='bar', color='green')
    plt.title('Total Sales Volume by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Total Sales Volume')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def plot_top_products_by_gender_section(df):
    """
    Plots top products by sales volume in each gender section.

    Parameters:
    - df (pd.DataFrame): Input DataFrame.
    """
    top_20_by_terms = df.groupby('terms').head(20)
    for gender in ['MAN', 'WOMAN']:
        top_by_gender = top_20_by_terms[top_20_by_terms['section'] == gender]

        plt.figure(figsize=(10, 6))
        for term, data in top_by_gender.groupby('terms'):
            if gender == 'MAN':
                plt.barh(data['name'], data['Sales Volume'], label=term)
            else:
                plt.bar(data['name'], data['Sales Volume'], label=term)

        if gender == 'MAN':
            plt.title('Category Products by Sales Volume in Man Section')
        else:
            plt.title('Category Products by Sales Volume in Woman Section')
        
        plt.xlabel('Sales Volume')
        plt.ylabel('Product Name')
        plt.xticks(rotation=45, ha='right')
        plt.legend(title='Product Category', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.show()
