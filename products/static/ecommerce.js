
$(document).ready(function () {
        const contactForm = $('.contact-form')
        const contactFormMethod = contactForm.attr('method')
        const contactFormEndpoint = contactForm.attr('action')
        contactForm.submit(function (event) {
            event.preventDefault()
            let contactFormData = contactForm.serialize()
            const thisForm = $(this)
            $.ajax({
                url: contactFormEndpoint,
                data: contactFormData,
                method: contactFormMethod,
                success: function (data) {
                    thisForm[0].reset()
                    $.alert({
                        title: "Success",
                        content: "Thanks for your submission",
                        theme: "modern"
                    })
                },
                error: function (error) {
                    $.alert({
                        title: "Failure",
                        content: "Check it one more time, please",
                        theme: "modern"
                    })
                }
            })
        })


        const searchForm = $('.search-form')
        const searchInput = searchForm.find('[name="search"]')
        let typingTimer
        const typingInterval = 2500
        const searchBtn = searchForm.find("[type='submit']")

        searchInput.keyup(function (event) {
            clearTimeout(typingTimer)
            typingTimer = setTimeout(performSearch, typingInterval)
        })
        searchInput.keydown(function (event) {
            clearTimeout(typingTimer)

        })

        function doSearch() {
            searchBtn.addClass('disabled')
            searchBtn.html("<i class='fa fa-spin fa-spinner'> </i> Searching...")

        }

        function performSearch() {
            doSearch()
            let query = searchInput.val()
            window.location.href = 'search/?search=' + query
        }






        const productForm = $(`#form-product-ajax`)


        productForm.submit(function (event) {
            event.preventDefault();
            const thisForm = $(this)
            const action = thisForm.attr('action')
            const method = thisForm.attr('method')
            const formData = thisForm.serialize()
            const actionEndpoint = thisForm.attr('data-endpoint')

            $.ajax({

                url: action,
                method: "POST",
                data: formData,
                success: function (data) {
                    console.log('Success', data)
                    const submitSpan = thisForm.find('.submit-span')
                    if (data.added) {
                        submitSpan.html('In cart <button type="submit" class="btn btn-danger">Remove</button>')

                    } else {
                        submitSpan.html('<button type="submit" class="btn btn-primary">Add to cart</button>')
                    }
                    let navbarCounter = $('.navbar-cart-count')
                    navbarCounter.text(data.cartItemCount)
                    let currentPath = window.location.href
                    if (currentPath.indexOf('cart') != -1) {
                        updateCart()
                    }
                },
                error: function (errorData) {
                    console.log('An error occured - ', errorData)
                }

            })

        })

        function updateCart() {
            console.log('In current cart')
            const cartTable = $('.cart-table')
            const cartBody = cartTable.find('.cart-body')
            let productRows = cartBody.find('.cart-products')
            let currentUrl = window.location.href
            let updateCartUrl = '/cart/api'
            let updateCartMethod = "GET"
            let data = {}
            $.ajax({
                url: updateCartUrl,
                method: updateCartMethod,
                data: data,
                success: function (data) {
                    console.log('success')
                    console.log(data)
                    if (data.products.length > 0) {
                        productRows.html('')
                        cartBody.prepend('<tr><td colspan=3> Coming soon </td></tr>')
                        cartBody.find('.cart-total').text(data.total)
                    } else {
                        window.location.href = currentUrl
                    }
                },
                error: function (errorData) {
                    $.alert('An error occured')
                    console.log(errorData)
                }

            })

        }

    })
 