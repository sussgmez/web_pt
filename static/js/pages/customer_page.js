async function submit_form(form) {
    await fetch(form.action, {
        method: form.method,
        body: new FormData(form)
    })
    .finally(() => {
        get_customer_list()
    })
}

async function get_customer_form(url, id_div) {
    await fetch(url)
    .then(response => {
        return response.text()
    })
    .then(data => {
        $(id_div).show();
        $(id_div).html(data);
    })
    .finally(() => {
        $(".btn-close-form").click(function (e) { 
            $(id_div).hide();
        });
        $(id_div).children('form').submit(function (e) { 
            e.preventDefault();
            submit_form(this)
            $(id_div).html('');
            $(id_div).hide();
        });
    })
}

async function get_customer_list(num_page=1) {
    await fetch(`../customer/list?page=${num_page}`)
    .then(response => {
        return response.text()
    })
    .then(data => {
        $('#id_customer_list').html(data);
    })
    .finally(() => {
        // Customer update
        $('.btn-options-customer-update').click(function (e) {
            customer_menu = $($(this).parents('.customer')).children('.customer-menu')
            if ($(customer_menu).is(":hidden")) {
                $('.options-menu').hide();
                $(customer_menu).show()
                e.stopPropagation()
            }
        });
    })
}

async function check_contract_number(value) {
    if (parseInt(value) >= 1000000 && parseInt(value) <= 1099999) {
        await fetch(`../customer/update/${value}`)
        .then(response => {
            if (!response.ok) {
                $("#id_btn_create_customer").prop('disabled', false);
                $('#id_check_contract_number').removeClass('status-invalid');
                $('#id_check_contract_number').removeClass('status-waiting');
                $('#id_check_contract_number').addClass('status-valid');
                $('#id_check_contract_number').html("<p>Nro. De Contrato válido.</p>");
            } else {
                $("#id_btn_create_customer").prop('disabled', true);
                $('#id_check_contract_number').addClass('status-invalid');
                $('#id_check_contract_number').removeClass('status-waiting');
                $('#id_check_contract_number').removeClass('status-valid');
                $('#id_check_contract_number').html("<p>Nro. De Contrato ya existe.</p>");
            }
        })
    } else {
        $("#id_btn_create_customer").prop('disabled', true);
        $('#id_check_contract_number').removeClass('status-invalid');
        $('#id_check_contract_number').addClass('status-waiting');
        $('#id_check_contract_number').removeClass('status-valid');
        $('#id_check_contract_number').html("<p>Ingrese un nro. de contrato válido.</p>");
    }
}

$(document).ready(function () {

    // Customer create
    $('#id_btn_customers_create').click(function (e) { 
        if ($("#id_customer_create_options").is(":hidden")) {
            $("#id_customer_create_options").show()
            e.stopPropagation()
        }
    });
    $(document).click(function (e) { 
        $('.options-menu').hide();
    });

    get_customer_list()
    // 
    // get_customer_form('../customer/create', '#id_customer_create')

    
});