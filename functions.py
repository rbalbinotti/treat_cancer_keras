def pre_process(data, col1='gene', col2='variation', col3='clinical_evidence', target_col=None):
    """
        Combine data columns and adjust column classification
    """

    data['combined_text'] = data[col1] + " " + data[col2] + " " + data[col3]

    # Adjust class to 0 - 8 it's necessary by keras to_categorical
    if target_col == None:
        data = data[['combined_text']]

    else:
        data['class_adjusted'] = data[target_col] - 1
        data = data[['combined_text', 'class_adjusted']]

    return data

