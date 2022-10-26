from h2o_wave import Q, main, app, ui


@app('/calculator')
async def serve(q: Q):
    answer = ""
    is_add_clicked = False

    if q.args.add:
        is_add_clicked = True
        first = q.args.firstTextbox
        second = q.args.secondTextbox
        try:
            answer = int(first) + int(second)
        except Exception as e:
            answer = "Enter valid input"
        finally:
            pass
            #todo clear text boxes

    elif q.args.subtract:
        first = q.args.firstTextbox
        second = q.args.secondTextbox
        try:
            answer = int(first) - int(second)
        except Exception as e:
            answer = "Enter valid input"
        finally:
            pass
            #todo clear text boxes


    if not q.client.initialized:
        q.client.initialized = True
        q.page['first_value'] = ui.form_card(
            box='1 1 2 2',
            items=[ui.textbox(name='firstTextbox', label='Enter first value', value='0')]
        )

        q.page['second_value'] = ui.form_card(
            box='1 2 2 2',
            items=[ui.textbox(name='secondTextbox', label='Enter second value', value='0')]
        )

        q.page['add'] = ui.form_card(
            box='1 3 2 2',
            items=[
                ui.button(
                    name='add',
                    label='Add',
                    primary=True,
                ),
            ]
        )

        q.page['subtract'] = ui.form_card(
            box='2 3 1 2',
            items=[
                ui.button(
                    name='subtract',
                    label='Subtract',
                    primary=True,
                ),
            ]
        )

        q.page['answer'] = ui.article_card(
            box='1 4 2 2',
            title='Answer',
            content=f'Answer is {answer}'
        )
    else:
        q.page['answer'].content = f'Answer is {answer}'
        print(is_add_clicked)
        if is_add_clicked:
            val = q.page['first_value'].textbox.value

    await q.page.save()
